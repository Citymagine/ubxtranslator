"""Predefined message classes"""

from . import core

__all__ = ['ACK_CLS', 'NAV_CLS', ]

ACK_CLS = core.Cls(0x05, 'ACK', [
    core.Message(0x01, 'ACK', [
        core.Field('clsID', 'U1'),
        core.Field('msgID', 'U1'),
    ]),
    core.Message(0x01, 'NAK', [
        core.Field('clsID', 'U1'),
        core.Field('msgID', 'U1'),
    ])
])

NAV_CLS = core.Cls(0x01, 'NAV', [
    core.Message(0x60, 'AOPSTATUS', [
        core.Field('iTOW', 'U4'),
        core.Field('aopCfg', 'U1'),
        core.Field('status', 'U1'),
        core.PadByte(repeat=9),
    ]),
    core.Message(0x05, 'ATT', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('roll', 'I4'),
        core.Field('pitch', 'I4'),
        core.Field('heading', 'I4'),
        core.Field('accRoll', 'U4'),
        core.Field('accPitch', 'U4'),
        core.Field('accHeading', 'U4'),
    ]),
    core.Message(0x22, 'CLOCK', [
        core.Field('iTOW', 'U4'),
        core.Field('clkB', 'I4'),
        core.Field('clkD', 'I4'),
        core.Field('tAcc', 'U4'),
        core.Field('fAcc', 'U4'),
    ]),
    core.Message(0x04, 'DOP', [
        core.Field('iTOW', 'U4'),
        core.Field('gDOP', 'U2'),
        core.Field('pDOP', 'U2'),
        core.Field('tDOP', 'U2'),
        core.Field('vDOP', 'U2'),
        core.Field('hDOP', 'U2'),
        core.Field('nDOP', 'U2'),
        core.Field('eDOP', 'U2'),
    ]),
    core.Message(0x61, 'EOE', [
        core.Field('iTOW', 'U4'),
    ]),
    core.Message(0x13, 'HPPOSECEF', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('iTOW', 'U4'),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('ecefXHp', 'I1'),
        core.Field('ecefYHp', 'I1'),
        core.Field('ecefZHp', 'I1'),
        core.PadByte(),
        core.Field('pAcc', 'U4'),
    ]),
    core.Message(0x14, 'HPPOSLLH', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('iTOW', 'U4'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('lonHp', 'I1'),
        core.Field('latHp', 'I1'),
        core.Field('heightHp', 'I1'),
        core.Field('hMSLHp', 'I1'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
    ]),
    core.Message(0x09, 'ODO', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('iTOW', 'U4'),
        core.Field('distance', 'U4'),
        core.Field('totalDistance', 'U4'),
        core.Field('distanceStd', 'U4'),
    ]),
    core.Message(0x01, 'POSECEF', [
        core.Field('iTOW', 'U4'),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('pAcc', 'U4'),
    ]),
    core.Message(0x02, 'POSLLH', [
        core.Field('iTOW', 'U4'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
    ]),
    core.Message(0x07, 'PVT', [
        core.Field('iTOW', 'U4'),
        core.Field('year', 'U2'),
        core.Field('month', 'U1'),
        core.Field('day', 'U1'),
        core.Field('hour', 'U1'),
        core.Field('min', 'U1'),
        core.Field('sec', 'U1'),
        core.BitField('valid', 'X1', [
            core.Flag('validDate', 0, 1),
            core.Flag('validTime', 1, 2),
            core.Flag('fullyResolved', 2, 3),
            core.Flag('validMag', 3, 4),
        ]),
        core.Field('tAcc', 'U4'),
        core.Field('nano', 'I4'),
        core.Field('fixType', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('gnssFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('headVehValid', 2, 5),
            core.Flag('carrSoln', 6, 8),
        ]),
        core.BitField('flags2', 'X1', [
            core.Flag('confirmedAvai', 5, 6),
            core.Flag('confirmedDate', 6, 7),
            core.Flag('confirmedTime', 7, 8),
        ]),
        core.Field('numSV', 'U1'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
        core.Field('velN', 'I4'),
        core.Field('velE', 'I4'),
        core.Field('velD', 'I4'),
        core.Field('gSpeed', 'I4'),
        core.Field('headMot', 'I4'),
        core.Field('sAcc', 'U4'),
        core.Field('headAcc', 'U4'),
        core.Field('pDOP', 'U2'),
        core.PadByte(5),
        core.Field('headVeh', 'I4'),
        core.Field('magDec', 'I2'),
        core.Field('magAcc', 'U2'),
    ]),
    core.Message(0x3C, 'RELPOSNED', [
        core.Field('version', 'U1'),
        core.PadByte(),
        core.Field('refStationId', 'U2'),
        core.Field('iTOW', 'U4'),
        core.Field('relPosN', 'I4'),
        core.Field('relPosE', 'I4'),
        core.Field('relPosD', 'I4'),
        core.Field('relPosHPN', 'I1'),
        core.Field('relPosHPE', 'I1'),
        core.Field('relPosHPD', 'I1'),
        core.PadByte(),
        core.Field('accN', 'U4'),
        core.Field('accE', 'U4'),
        core.Field('accD', 'U4'),
        core.BitField('flags', 'X4', [
            core.Flag('gnssFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('relPosValid', 2, 3),
            core.Flag('carrSoln', 3, 5),
            core.Flag('isMoving', 5, 6),
            core.Flag('refPosMiss', 6, 7),
            core.Flag('refObsMiss', 7, 8),
        ]),
    ]),
])
