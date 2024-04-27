import sys
import struct


DATA_TYPE_INT = 0
DATA_TYPE_UINT = 1
DATA_TYPE_FLOAT = 2
DATA_TYPE_COMMAND = 3


class Result:
    def __init__(self, ok=None, err=None):
        self.ok = ok
        self.err = err


class MsgTypeConfig:
    def __init__(self, msg_type: int = None, msg_name: str = None, data_type: int = None, size_bytes: int = None):
        self.msg_type = msg_type
        self.msg_name = msg_name
        self.data_type = data_type
        self.size_bytes = size_bytes


class DeviceMsg:
    def __init__(self, seq_number: int = None, msg_value: int = None, b64_msg_value: str = None, config: MsgTypeConfig = MsgTypeConfig()):
        self.seq_number = seq_number
        self.msg_value = msg_value
        self.b64_msg_value = b64_msg_value
        self.config = config


class LtdDriver_0x87:
    PACKET_MIN_SIZE = 11
    DATA_START = 7
    PROTOCOL_VERSION = 0x87

    driver_msg_type_config_map: dict[int, MsgTypeConfig] = {}
    msg_seq_number: int = 0

    # for search optimization
    msg_type_set = set()
    msg_name_set = set()
    data_type_set = {0, 1, 2, 3}

    def __init__(self, _driver_msg_types: list[MsgTypeConfig]) -> None:
        self.msg_type_set = set(config.msg_type for config in _driver_msg_types)
        self.msg_name_set = set(config.msg_name for config in _driver_msg_types)
        self.driver_msg_type_config_map = {config.msg_type: config for config in _driver_msg_types}

    @staticmethod
    def _cx_b64encode(data: bytes) -> bytes:
        if sys.implementation.name == 'cpython':
            from base64 import b64encode  # type: ignore
            return b64encode(data)
        elif sys.implementation.name == 'micropython':
            from ubinascii import b2a_base64  # type: ignore
            return b2a_base64(data)

    @staticmethod
    def _get_binary_parser(size_bytes: int, data_type: int) -> Result:
        PARSERS_MAP = {
            1: {
                DATA_TYPE_INT: 'b',
                DATA_TYPE_UINT: 'B',
                DATA_TYPE_COMMAND: 'B',
            },
            2: {
                DATA_TYPE_INT: '<h',
                DATA_TYPE_UINT: '<H',
            },
            4: {
                DATA_TYPE_INT: '<l',
                DATA_TYPE_UINT: '<L',
                DATA_TYPE_FLOAT: '<f',
            },
            8: {
                DATA_TYPE_INT: '<q',
                DATA_TYPE_UINT: '<Q',
                DATA_TYPE_FLOAT: '<d',
            },
        }

        if size_bytes not in PARSERS_MAP:
            return Result(err=f"Protocol Version: {LtdDriver_0x87.PROTOCOL_VERSION} Do not Support Data Size: {size_bytes} Bytes")
        map_lvl_2 = PARSERS_MAP[size_bytes]
        if data_type not in map_lvl_2:
            return Result(err=f"No Binary Parser was Found for: data_type={data_type}, size_bytes={size_bytes}")
        return Result(ok=PARSERS_MAP[size_bytes][data_type])

    @staticmethod
    def _bin_byte(byte: int) -> str:
        _bin_byte = bin(byte)[2:]
        padded_bin_byte = _bin_byte.rjust(8, '0')
        return padded_bin_byte

    @staticmethod
    def _compute_crc16(buffer: bytes) -> int:
        CRC16_POLYNOMIAL = [
            0x0000, 0x1189, 0x2312, 0x329B, 0x4624, 0x57AD, 0x6536, 0x74BF,
            0x8C48, 0x9DC1, 0xAF5A, 0xBED3, 0xCA6C, 0xDBE5, 0xE97E, 0xF8F7,
            0x1081, 0x0108, 0x3393, 0x221A, 0x56A5, 0x472C, 0x75B7, 0x643E,
            0x9CC9, 0x8D40, 0xBFDB, 0xAE52, 0xDAED, 0xCB64, 0xF9FF, 0xE876,
            0x2102, 0x308B, 0x0210, 0x1399, 0x6726, 0x76AF, 0x4434, 0x55BD,
            0xAD4A, 0xBCC3, 0x8E58, 0x9FD1, 0xEB6E, 0xFAE7, 0xC87C, 0xD9F5,
            0x3183, 0x200A, 0x1291, 0x0318, 0x77A7, 0x662E, 0x54B5, 0x453C,
            0xBDCB, 0xAC42, 0x9ED9, 0x8F50, 0xFBEF, 0xEA66, 0xD8FD, 0xC974,
            0x4204, 0x538D, 0x6116, 0x709F, 0x0420, 0x15A9, 0x2732, 0x36BB,
            0xCE4C, 0xDFC5, 0xED5E, 0xFCD7, 0x8868, 0x99E1, 0xAB7A, 0xBAF3,
            0x5285, 0x430C, 0x7197, 0x601E, 0x14A1, 0x0528, 0x37B3, 0x263A,
            0xDECD, 0xCF44, 0xFDDF, 0xEC56, 0x98E9, 0x8960, 0xBBFB, 0xAA72,
            0x6306, 0x728F, 0x4014, 0x519D, 0x2522, 0x34AB, 0x0630, 0x17B9,
            0xEF4E, 0xFEC7, 0xCC5C, 0xDDD5, 0xA96A, 0xB8E3, 0x8A78, 0x9BF1,
            0x7387, 0x620E, 0x5095, 0x411C, 0x35A3, 0x242A, 0x16B1, 0x0738,
            0xFFCF, 0xEE46, 0xDCDD, 0xCD54, 0xB9EB, 0xA862, 0x9AF9, 0x8B70,
            0x8408, 0x9581, 0xA71A, 0xB693, 0xC22C, 0xD3A5, 0xE13E, 0xF0B7,
            0x0840, 0x19C9, 0x2B52, 0x3ADB, 0x4E64, 0x5FED, 0x6D76, 0x7CFF,
            0x9489, 0x8500, 0xB79B, 0xA612, 0xD2AD, 0xC324, 0xF1BF, 0xE036,
            0x18C1, 0x0948, 0x3BD3, 0x2A5A, 0x5EE5, 0x4F6C, 0x7DF7, 0x6C7E,
            0xA50A, 0xB483, 0x8618, 0x9791, 0xE32E, 0xF2A7, 0xC03C, 0xD1B5,
            0x2942, 0x38CB, 0x0A50, 0x1BD9, 0x6F66, 0x7EEF, 0x4C74, 0x5DFD,
            0xB58B, 0xA402, 0x9699, 0x8710, 0xF3AF, 0xE226, 0xD0BD, 0xC134,
            0x39C3, 0x284A, 0x1AD1, 0x0B58, 0x7FE7, 0x6E6E, 0x5CF5, 0x4D7C,
            0xC60C, 0xD785, 0xE51E, 0xF497, 0x8028, 0x91A1, 0xA33A, 0xB2B3,
            0x4A44, 0x5BCD, 0x6956, 0x78DF, 0x0C60, 0x1DE9, 0x2F72, 0x3EFB,
            0xD68D, 0xC704, 0xF59F, 0xE416, 0x90A9, 0x8120, 0xB3BB, 0xA232,
            0x5AC5, 0x4B4C, 0x79D7, 0x685E, 0x1CE1, 0x0D68, 0x3FF3, 0x2E7A,
            0xE70E, 0xF687, 0xC41C, 0xD595, 0xA12A, 0xB0A3, 0x8238, 0x93B1,
            0x6B46, 0x7ACF, 0x4854, 0x59DD, 0x2D62, 0x3CEB, 0x0E70, 0x1FF9,
            0xF78F, 0xE606, 0xD49D, 0xC514, 0xB1AB, 0xA022, 0x92B9, 0x8330,
            0x7BC7, 0x6A4E, 0x58D5, 0x495C, 0x3DE3, 0x2C6A, 0x1EF1, 0x0F78,
        ]

        res = 0xffff
        for b in buffer:
            res = (res >> 8) ^ CRC16_POLYNOMIAL[(res ^ b) & 0xff]
        return (~res) & 0xffff

    @staticmethod
    def _bin_parse(buffer: bytes, data_type: int) -> Result:
        if data_type == DATA_TYPE_FLOAT and len(buffer) in [1, 2]:
            return {"err": f"Can not Parse Buffer of Size [{len(buffer)}] to FLOAT"}

        bin_parser_res = LtdDriver_0x87._get_binary_parser(len(buffer), data_type)
        if bin_parser_res.err:
            return bin_parser_res

        format_specifier = bin_parser_res.ok
        parsed_value = struct.unpack(format_specifier, buffer)[0]
        return Result(ok=parsed_value)

    @staticmethod
    def _u16_to_2u8(num: int) -> Result:
        if num < 0 or num > 65535:
            return Result(err='Number Is not Valid u16')

        lsb = num & 0xFF
        msb = (num >> 8) & 0xFF
        byte_array = bytes([lsb, msb])
        return Result(ok=byte_array)

    def _gen_cfg1(self, data_type: int, size_bytes: int, msg_type: int) -> Result:
        # data type bits
        data_type_bits = bin(data_type)[2:].zfill(2)

        # data length bits
        binary_parser_res = LtdDriver_0x87._get_binary_parser(size_bytes, DATA_TYPE_INT)
        if binary_parser_res.err:
            return Result(err='Invalid Data Length Bits')
        data_length_bits = bin(int(size_bytes).bit_length() - 1)[2:].zfill(2)

        # msg type bits
        if msg_type not in self.msg_type_set:
            return Result(err='Invalid Msg Type Bits')
        msg_type_bits = bin(msg_type)[2:].zfill(4)

        # concatenate bits
        cfg1_bits = data_type_bits + data_length_bits + msg_type_bits
        return Result(ok=int(cfg1_bits, 2))

    def get_msg_type_by_name(self, msg_name: str) -> int:
        ''' do not use this function extensively, complexity = O(N) '''
        if msg_name not in self.msg_name_set:
            return -1
        target_config = [x for x in self.driver_msg_type_config_map.values() if x.msg_name == msg_name]
        if not target_config:
            return -1
        return target_config[0].msg_type

    def reset_seq_number(self):
        self.msg_seq_number = 0

    def encode_packet(self, msg_type: int, msg_value: int) -> Result:
        if msg_type not in self.msg_type_set:
            return Result(err='Unknown msg_type')

        cfg2 = '00000000'
        size_bytes = self.driver_msg_type_config_map[msg_type].size_bytes
        data_type = self.driver_msg_type_config_map[msg_type].data_type
        start_seg = bytes([LtdDriver_0x87.PROTOCOL_VERSION, LtdDriver_0x87.PROTOCOL_VERSION, (LtdDriver_0x87.PACKET_MIN_SIZE + size_bytes)])

        result = LtdDriver_0x87._u16_to_2u8(LtdDriver_0x87.msg_seq_number)
        if result.err:
            return result
        seq_number_seg: bytes = result.ok

        result = self._gen_cfg1(data_type, size_bytes, msg_type)
        if result.err:
            return result
        cfg_seg = bytes([result.ok, int(cfg2, 2)])

        bin_parser_res = LtdDriver_0x87._get_binary_parser(size_bytes, data_type)
        if bin_parser_res.err:
            return bin_parser_res
        data_payload = struct.pack(bin_parser_res.ok, msg_value)

        seg_1 = start_seg + seq_number_seg + cfg_seg + data_payload
        # compute crc16
        crc16 = LtdDriver_0x87._compute_crc16(seg_1)
        result = LtdDriver_0x87._u16_to_2u8(crc16)
        if result.err:
            return result
        crc16_bytes: bytes = result.ok
        # construct final packet
        end_seg = bytes([0x0D, 0x0A])
        packet = seg_1 + crc16_bytes + end_seg
        self.msg_seq_number = (self.msg_seq_number + 1) % 0xFFFF
        return Result(ok=packet)

    def decode_packet(slef, packet: bytearray) -> Result:
        if len(packet) <= LtdDriver_0x87.PACKET_MIN_SIZE:
            return Result(err='Packet Too Small')

        # CRC-16 check
        packet_crc16_bytes = packet[-4:-2]
        packet_crc16 = int.from_bytes(packet_crc16_bytes, byteorder='little')
        computed_crc16 = LtdDriver_0x87._compute_crc16(packet[:-4])
        if packet_crc16 != computed_crc16:
            return Result(err={
                'msg': 'Invalid CRC-16',
                'detail': f'packet_crc16={packet_crc16}, computed_crc16={computed_crc16}',
            })

        # packet start bytes
        version_byte_1 = packet[0]
        version_byte_2 = packet[1]
        if version_byte_1 != version_byte_2:
            return Result(err='Version Bytes Mismatch')

        device_msg = DeviceMsg()

        # packet size
        if len(packet) != packet[2]:
            return Result(err={
                'msg': 'Packet Size Mismatch',
                'detail': f'packet[2]={packet[2]}, packet.length={len(packet)}',
            })
        device_msg.config.size_bytes = packet[2]

        # packet sequence number
        seq_number_bytes = packet[3:5]
        result = LtdDriver_0x87._bin_parse(seq_number_bytes, DATA_TYPE_UINT)
        if result.err:
            return result
        device_msg.seq_number = result.ok

        # decode config byte 1
        cfg1_bits = LtdDriver_0x87._bin_byte(packet[5])

        # data type
        data_type_bits = cfg1_bits[:2]
        data_type = int(data_type_bits, 2)
        if data_type not in slef.data_type_set:
            return Result(err={
                'msg': 'Invalid Data Type Bits',
                'detail': f'data_type_bits={data_type_bits}',
            })
        device_msg.config.data_type = data_type

        # data length
        size_bytes_bits = cfg1_bits[2:4]
        size_bytes = 2 ** int(size_bytes_bits, 2)
        if size_bytes != len(packet) - LtdDriver_0x87.PACKET_MIN_SIZE:
            return Result(err={
                'msg': 'Invalid Data Length Bits',
                'detail': f'data_length_bits={size_bytes}, Packet Data Size: {len(packet) - LtdDriver_0x87.PACKET_MIN_SIZE}',
            })
        device_msg.config.size_bytes = size_bytes

        # msg type
        msg_type_bits = cfg1_bits[4:8]
        msg_type = int(msg_type_bits, 2)
        if msg_type not in slef.msg_type_set:
            return Result(err={
                'msg': 'Invalid Msg Type Bits',
                'detail': f'msg_type_bits={msg_type_bits}',
            })
        device_msg.config.msg_type = msg_type

        # parse data payload
        data_payload = packet[LtdDriver_0x87.DATA_START:LtdDriver_0x87.DATA_START + size_bytes]

        # base64 encode data payload
        device_msg.b64_msg_value = LtdDriver_0x87._cx_b64encode(data_payload).decode('utf-8')

        result = LtdDriver_0x87._bin_parse(data_payload, data_type)
        if result.err:
            return result
        device_msg.msg_value = result.ok

        return Result(ok=device_msg)
