"""Some sample valid navigation packets."""

sample_packets = [
    b'\x01\x07\\\x00\xe8\xcb\x85\x07\xe3\x07\x06\x03\x0b\x03\x0b7\'\x00\x00\x00\x8d\x02\x02\x00\x03!\xeb\x07\xa8\x92c[u#v\xee.\xd9\x00\x00VU\x00\x00\xe55\x00\x00bH\x00\x00\x10\x00\x00\x00\x8e\xff\xff\xff\xe0\xff\xff\xffs\x00\x00\x00M\xc6\xc5\x00\x9a\x03\x00\x00L91\x00\xed\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00(\x8f\xb5b',
    b'\x01\x07\\\x00\xd0\xcf\x85\x07\xe3\x07\x06\x03\x0b\x03\x0c7\'\x00\x00\x00\xe8\x1c\x02\x00\x03!\xeb\x07\xd0\x92c[\x92#v\xee\xfc\xd7\x00\x00$T\x00\x00\r6\x00\x00\xc4H\x00\x00\xc4\x00\x00\x00\x83\x00\x00\x00\xea\xff\xff\xff\xec\x00\x00\x00M\xc6\xc5\x00M\x03\x00\x00L91\x00\xed\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\xd5\x87\xb5b',
    b'\x01\x07\\\x00\xb8\xd3\x85\x07\xe3\x07\x06\x03\x0b\x03\r7\'\x00\x00\x00@7\x02\x00\x03!\xeb\x07\xf5\x92c[\x93#v\xee\xd8\xd8\x00\x00\x01U\x00\x00>6\x00\x00"I\x00\x00f\x00\x00\x00\x11\x01\x00\x00\xe6\xff\xff\xff#\x01\x00\x00M\xc6\xc5\x00\x1b\x03\x00\x00L91\x00\xed\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\xd9\xcd\xb5b',
    b'\x01\x07\\\x00\xa0\xd7\x85\x07\xe3\x07\x06\x03\x0b\x03\x0e7\'\x00\x00\x00\x98Q\x02\x00\x03!\xeb\x07I\x93c[\xb9#v\xeep\xda\x00\x00\x98V\x00\x00_6\x00\x00xI\x00\x00\xf3\x00\x00\x00c\x02\x00\x00\xdd\xff\xff\xff\x92\x02\x00\x00M\xc6\xc5\x00\x1a\x03\x00\x00L91\x00\xed\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\xa2\xbb\xb5b',
    b'\x01\x07\\\x00\x88\xdb\x85\x07\xe3\x07\x06\x03\x0b\x03\x0f7\'\x00\x00\x00\xedk\x02\x00\x03!\xeb\x08;\x93c[\xaf#v\xee\xb2\xdb\x00\x00\xdbW\x00\x00y6\x00\x00lI\x00\x00\xc8\xff\xff\xff1\x01\x00\x00\xda\xff\xff\xff6\x01\x00\x00M\xc6\xc5\x00\xbf\x03\x00\x00L91\x00\xb6\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00)~\xb5b',
    b'\x01\x07\\\x00p\xdf\x85\x07\xe3\x07\x06\x03\x0b\x03\x107\'\x00\x00\x00@\x86\x02\x00\x03!\xeb\x07g\x93c[\xa9#v\xee \xdd\x00\x00HY\x00\x00\xc96\x00\x00\xc5I\x00\x00\xa2\xff\xff\xff\xf8\x01\x00\x00\xd3\xff\xff\xff\x00\x02\x00\x00M\xc6\xc5\x00\xdb\x03\x00\x00L91\x00\xed\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\xe9\x8b\xb5b',
    b'\x01\x07\\\x00X\xe3\x85\x07\xe3\x07\x06\x03\x0b\x03\x117\'\x00\x00\x00\x90\xa0\x02\x00\x03!\xeb\x08o\x93c[\xc6#v\xee\x1d\xde\x00\x00FZ\x00\x00\r7\x00\x00\x0cJ\x00\x00\x05\x00\x00\x00\x8e\x01\x00\x00\xd1\xff\xff\xff\x8e\x01\x00\x00M\xc6\xc5\x00\x9d\x03\x00\x00L91\x00\xda\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00&\xc7\xb5b',
    b'\x01\x07\\\x00@\xe7\x85\x07\xe3\x07\x06\x03\x0b\x03\x127\'\x00\x00\x00\xdd\xba\x02\x00\x03!\xeb\x071\x93c[\xe5#v\xeef\xdf\x00\x00\x8e[\x00\x00\'7\x00\x00LJ\x00\x00\xdb\xff\xff\xff)\x00\x00\x00\xcb\xff\xff\xff8\x00\x00\x00M\xc6\xc5\x00.\x03\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\xfaT\xb5b',
    b'\x01\x07\\\x00(\xeb\x85\x07\xe3\x07\x06\x03\x0b\x03\x137\'\x00\x00\x00*\xd5\x02\x00\x03!\xeb\x07\xc5\x92c[\xef#v\xee\x86\xe0\x00\x00\xaf\\\x00\x0057\x00\x00\x80J\x00\x008\xff\xff\xff \xfe\xff\xff\xc5\xff\xff\xff\x07\x02\x00\x00M\xc6\xc5\x00\x1d\x03\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00{/\xb5b',
    b'\x01\x07\\\x00\x10\xef\x85\x07\xe3\x07\x06\x03\x0b\x03\x147(\x00\x00\x00{\xef\x02\x00\x03!\xeb\x07\xcc\x92c[\xcb#v\xee\xae\xe0\x00\x00\xd6\\\x00\x00l7\x00\x00\xb3J\x00\x00\xb9\xfe\xff\xff\x18\xff\xff\xff\xc6\xff\xff\xff\x91\x01\x00\x00M\xc6\xc5\x00B\x03\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\x98l\xb5b',
    b'\x01\x07\\\x00\xf8\xf2\x85\x07\xe3\x07\x06\x03\x0b\x03\x157(\x00\x00\x00\xcd\t\x03\x00\x03!\xeb\x07\xe8\x92c[\xa0#v\xee.\xe0\x00\x00V\\\x00\x00\x827\x00\x00\xddJ\x00\x00l\xfe\xff\xff>\x00\x00\x00\xca\xff\xff\xff\x99\x01\x00\x00M\xc6\xc5\x00\xf7\x03\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\xbf%\xb5b',
    b'\x01\x07\\\x00\xe0\xf6\x85\x07\xe3\x07\x06\x03\x0b\x03\x167(\x00\x00\x00\x1f$\x03\x00\x03!\xeb\x07\x08\x93c[\xc2#v\xee\xeb\xe0\x00\x00\x13]\x00\x00\x917\x00\x00\x01K\x00\x00|\xff\xff\xff\xff\x00\x00\x00\xc5\xff\xff\xff\x1f\x01\x00\x00M\xc6\xc5\x00#\x04\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\x8b\xf3\xb5b',
    b'\x01\x07\\\x00\xc8\xfa\x85\x07\xe3\x07\x06\x03\x0b\x03\x177(\x00\x00\x00p>\x03\x00\x03!\xeb\x07T\x93c[\xb6#v\xeeC\xe1\x00\x00k]\x00\x00\xb47\x00\x00,K\x00\x00k\xff\xff\xff:\x02\x00\x00\xc1\xff\xff\xffM\x02\x00\x00M\xc6\xc5\x00\x16\x04\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00l\xe3\xb5b',
    b'\x01\x07\\\x00\xb0\xfe\x85\x07\xe3\x07\x06\x03\x0b\x03\x187(\x00\x00\x00\xc0X\x03\x00\x03!\xeb\x07\x98\x93c[\xb9#v\xee2\xe0\x00\x00Z\\\x00\x00\xe57\x00\x00cK\x00\x00\xb6\xff\xff\xff\x19\x03\x00\x00\xc8\xff\xff\xff\x1c\x03\x00\x00M\xc6\xc5\x00\xf1\x03\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00*\x9c\xb5b',
    b'\x01\x07\\\x00\x98\x02\x86\x07\xe3\x07\x06\x03\x0b\x03\x197(\x00\x00\x00\x0es\x03\x00\x03!\xeb\x07\xf5\x93c[\x9d#v\xeej\xe0\x00\x00\x93\\\x00\x00\x1b8\x00\x00\x94K\x00\x00)\xff\xff\xff\xbb\x03\x00\x00\xc5\xff\xff\xff\xd3\x03\x00\x00M\xc6\xc5\x00\x17\x04\x00\x00L91\x00\xec\x00\x00\x006\xab,"M\xc6\xc5\x00\x00\x00\x00\x00\x8b\xfb\xb5b',
]