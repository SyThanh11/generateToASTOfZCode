# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u019b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\5\4d\n\4\3\5\3\5\3\5\5")
        buf.write("\5i\n\5\3\5\3\5\3\5\5\5n\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7{\n\7\3\7\3\7\5\7\177\n\7\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0085\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u0092\n\13\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u0098\n\f\3\f\3\f\5\f\u009c\n\f\3\f\3\f\5\f\u00a0\n\f")
        buf.write("\3\f\3\f\5\f\u00a4\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ab\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b3\n\16\3\17")
        buf.write("\3\17\5\17\u00b7\n\17\3\20\3\20\5\20\u00bb\n\20\3\20\3")
        buf.write("\20\3\20\5\20\u00c0\n\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00cb\n\21\3\22\3\22\3\22\5\22\u00d0")
        buf.write("\n\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24")
        buf.write("\u00db\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u00e7\n\26\3\26\3\26\3\26\3\26\5\26\u00ed")
        buf.write("\n\26\3\26\5\26\u00f0\n\26\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00f7\n\27\3\27\3\27\3\27\3\27\5\27\u00fd\n\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0106\n\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\5\33\u0112")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\5\34\u0119\n\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0129\n\36\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0130\n\37\3 \3 \3 \3 \3!\3!\3!\5!\u0139\n!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\5\"\u0142\n\"\3#\3#\3#\3#\3#\5#\u0149")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u0150\n$\3%\3%\3%\3%\3%\3%\7%\u0158")
        buf.write("\n%\f%\16%\u015b\13%\3&\3&\3&\3&\3&\3&\7&\u0163\n&\f&")
        buf.write("\16&\u0166\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u016e\n\'\f")
        buf.write("\'\16\'\u0171\13\'\3(\3(\3(\5(\u0176\n(\3)\3)\3)\5)\u017b")
        buf.write("\n)\3*\3*\3*\3*\5*\u0181\n*\3*\5*\u0184\n*\3*\3*\3*\3")
        buf.write("*\3*\5*\u018b\n*\3+\3+\3+\3+\3+\3+\3+\5+\u0194\n+\3,\6")
        buf.write(",\u0197\n,\r,\16,\u0198\3,\2\5HJL-\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TV\2\7\3\2\5\7\5\2\36\36 $&&\3\2\34\35\3\2\26\27\3\2\30")
        buf.write("\32\2\u01aa\2X\3\2\2\2\4_\3\2\2\2\6c\3\2\2\2\bm\3\2\2")
        buf.write("\2\no\3\2\2\2\ft\3\2\2\2\16\u0080\3\2\2\2\20\u0086\3\2")
        buf.write("\2\2\22\u0088\3\2\2\2\24\u0091\3\2\2\2\26\u0093\3\2\2")
        buf.write("\2\30\u00aa\3\2\2\2\32\u00ac\3\2\2\2\34\u00b6\3\2\2\2")
        buf.write("\36\u00bf\3\2\2\2 \u00ca\3\2\2\2\"\u00cf\3\2\2\2$\u00d3")
        buf.write("\3\2\2\2&\u00da\3\2\2\2(\u00dc\3\2\2\2*\u00e1\3\2\2\2")
        buf.write(",\u00fc\3\2\2\2.\u00fe\3\2\2\2\60\u0109\3\2\2\2\62\u010c")
        buf.write("\3\2\2\2\64\u010f\3\2\2\2\66\u0115\3\2\2\28\u011d\3\2")
        buf.write("\2\2:\u0128\3\2\2\2<\u012f\3\2\2\2>\u0131\3\2\2\2@\u0135")
        buf.write("\3\2\2\2B\u0141\3\2\2\2D\u0148\3\2\2\2F\u014f\3\2\2\2")
        buf.write("H\u0151\3\2\2\2J\u015c\3\2\2\2L\u0167\3\2\2\2N\u0175\3")
        buf.write("\2\2\2P\u017a\3\2\2\2R\u018a\3\2\2\2T\u0193\3\2\2\2V\u0196")
        buf.write("\3\2\2\2XY\5\4\3\2YZ\7\2\2\3Z\3\3\2\2\2[\\\5\6\4\2\\]")
        buf.write("\5\4\3\2]`\3\2\2\2^`\5\6\4\2_[\3\2\2\2_^\3\2\2\2`\5\3")
        buf.write("\2\2\2ad\5\b\5\2bd\5\26\f\2ca\3\2\2\2cb\3\2\2\2d\7\3\2")
        buf.write("\2\2ei\5\n\6\2fi\5\f\7\2gi\5\16\b\2he\3\2\2\2hf\3\2\2")
        buf.write("\2hg\3\2\2\2ij\3\2\2\2jk\5V,\2kn\3\2\2\2ln\5V,\2mh\3\2")
        buf.write("\2\2ml\3\2\2\2n\t\3\2\2\2op\7\t\2\2pq\7.\2\2qr\7\37\2")
        buf.write("\2rs\5D#\2s\13\3\2\2\2tu\5\20\t\2uz\7.\2\2vw\7+\2\2wx")
        buf.write("\5\24\13\2xy\7,\2\2y{\3\2\2\2zv\3\2\2\2z{\3\2\2\2{~\3")
        buf.write("\2\2\2|}\7\37\2\2}\177\5D#\2~|\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\r\3\2\2\2\u0080\u0081\7\n\2\2\u0081\u0084\7.\2\2\u0082")
        buf.write("\u0083\7\37\2\2\u0083\u0085\5D#\2\u0084\u0082\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0085\17\3\2\2\2\u0086\u0087\t\2")
        buf.write("\2\2\u0087\21\3\2\2\2\u0088\u0089\7.\2\2\u0089\u008a\7")
        buf.write("+\2\2\u008a\u008b\5\24\13\2\u008b\u008c\7,\2\2\u008c\23")
        buf.write("\3\2\2\2\u008d\u008e\7/\2\2\u008e\u008f\7-\2\2\u008f\u0092")
        buf.write("\5\24\13\2\u0090\u0092\7/\2\2\u0091\u008d\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\25\3\2\2\2\u0093\u0094\7\13\2\2\u0094")
        buf.write("\u0095\7.\2\2\u0095\u0097\7\'\2\2\u0096\u0098\5\30\r\2")
        buf.write("\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\u00a3\7(\2\2\u009a\u009c\5V,\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u00a4\5\64\33\2\u009e\u00a0\5V,\2\u009f\u009e\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a4\5")
        buf.write("8\35\2\u00a2\u00a4\5V,\2\u00a3\u009b\3\2\2\2\u00a3\u009f")
        buf.write("\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\27\3\2\2\2\u00a5\u00a6")
        buf.write("\5\32\16\2\u00a6\u00a7\7-\2\2\u00a7\u00a8\5\30\r\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00ab\5\32\16\2\u00aa\u00a5\3\2\2")
        buf.write("\2\u00aa\u00a9\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00ad\5")
        buf.write("\20\t\2\u00ad\u00b2\7.\2\2\u00ae\u00af\7+\2\2\u00af\u00b0")
        buf.write("\5\24\13\2\u00b0\u00b1\7,\2\2\u00b1\u00b3\3\2\2\2\u00b2")
        buf.write("\u00ae\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\33\3\2\2\2\u00b4")
        buf.write("\u00b7\5\36\20\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2")
        buf.write("\2\u00b6\u00b5\3\2\2\2\u00b7\35\3\2\2\2\u00b8\u00ba\5")
        buf.write(" \21\2\u00b9\u00bb\5V,\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\5\36\20\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00c0\5 \21\2\u00bf\u00b8\3\2\2\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00c0\37\3\2\2\2\u00c1\u00cb\5\"")
        buf.write("\22\2\u00c2\u00cb\5$\23\2\u00c3\u00cb\5*\26\2\u00c4\u00cb")
        buf.write("\5.\30\2\u00c5\u00cb\5\60\31\2\u00c6\u00cb\5\62\32\2\u00c7")
        buf.write("\u00cb\5\64\33\2\u00c8\u00cb\5\66\34\2\u00c9\u00cb\58")
        buf.write("\35\2\u00ca\u00c1\3\2\2\2\u00ca\u00c2\3\2\2\2\u00ca\u00c3")
        buf.write("\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c5\3\2\2\2\u00ca")
        buf.write("\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00c9\3\2\2\2\u00cb!\3\2\2\2\u00cc\u00d0\5\n\6")
        buf.write("\2\u00cd\u00d0\5\f\7\2\u00ce\u00d0\5\16\b\2\u00cf\u00cc")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d2\5V,\2\u00d2#\3\2\2\2\u00d3")
        buf.write("\u00d4\5&\24\2\u00d4\u00d5\7\37\2\2\u00d5\u00d6\5D#\2")
        buf.write("\u00d6\u00d7\5V,\2\u00d7%\3\2\2\2\u00d8\u00db\5(\25\2")
        buf.write("\u00d9\u00db\7.\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3")
        buf.write("\2\2\2\u00db\'\3\2\2\2\u00dc\u00dd\7.\2\2\u00dd\u00de")
        buf.write("\7+\2\2\u00de\u00df\5B\"\2\u00df\u00e0\7,\2\2\u00e0)\3")
        buf.write("\2\2\2\u00e1\u00e2\7\21\2\2\u00e2\u00e3\7\'\2\2\u00e3")
        buf.write("\u00e4\5D#\2\u00e4\u00e6\7(\2\2\u00e5\u00e7\5V,\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\5 \21\2\u00e9\u00ef\5,\27\2\u00ea\u00ec\7")
        buf.write("\22\2\2\u00eb\u00ed\5V,\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\5 \21\2\u00ef")
        buf.write("\u00ea\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0+\3\2\2\2\u00f1")
        buf.write("\u00f2\7\23\2\2\u00f2\u00f3\7\'\2\2\u00f3\u00f4\5D#\2")
        buf.write("\u00f4\u00f6\7(\2\2\u00f5\u00f7\5V,\2\u00f6\u00f5\3\2")
        buf.write("\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9")
        buf.write("\5 \21\2\u00f9\u00fa\5,\27\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f1\3\2\2\2\u00fc\u00fb\3\2\2\2")
        buf.write("\u00fd-\3\2\2\2\u00fe\u00ff\7\f\2\2\u00ff\u0100\7.\2\2")
        buf.write("\u0100\u0101\7\r\2\2\u0101\u0102\5D#\2\u0102\u0103\7\16")
        buf.write("\2\2\u0103\u0105\5D#\2\u0104\u0106\5V,\2\u0105\u0104\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108")
        buf.write("\5 \21\2\u0108/\3\2\2\2\u0109\u010a\7\17\2\2\u010a\u010b")
        buf.write("\5V,\2\u010b\61\3\2\2\2\u010c\u010d\7\20\2\2\u010d\u010e")
        buf.write("\5V,\2\u010e\63\3\2\2\2\u010f\u0111\7\b\2\2\u0110\u0112")
        buf.write("\5D#\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\5V,\2\u0114\65\3\2\2\2\u0115\u0116")
        buf.write("\7.\2\2\u0116\u0118\7\'\2\2\u0117\u0119\5B\"\2\u0118\u0117")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\7(\2\2\u011b\u011c\5V,\2\u011c\67\3\2\2\2\u011d")
        buf.write("\u011e\7\24\2\2\u011e\u011f\5V,\2\u011f\u0120\5\34\17")
        buf.write("\2\u0120\u0121\7\25\2\2\u0121\u0122\5V,\2\u01229\3\2\2")
        buf.write("\2\u0123\u0124\5<\37\2\u0124\u0125\7-\2\2\u0125\u0126")
        buf.write("\5:\36\2\u0126\u0129\3\2\2\2\u0127\u0129\5<\37\2\u0128")
        buf.write("\u0123\3\2\2\2\u0128\u0127\3\2\2\2\u0129;\3\2\2\2\u012a")
        buf.write("\u0130\7/\2\2\u012b\u0130\7\61\2\2\u012c\u0130\7\3\2\2")
        buf.write("\u012d\u0130\7\4\2\2\u012e\u0130\5> \2\u012f\u012a\3\2")
        buf.write("\2\2\u012f\u012b\3\2\2\2\u012f\u012c\3\2\2\2\u012f\u012d")
        buf.write("\3\2\2\2\u012f\u012e\3\2\2\2\u0130=\3\2\2\2\u0131\u0132")
        buf.write("\7+\2\2\u0132\u0133\5B\"\2\u0133\u0134\7,\2\2\u0134?\3")
        buf.write("\2\2\2\u0135\u0136\7.\2\2\u0136\u0138\7\'\2\2\u0137\u0139")
        buf.write("\5B\"\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\u013b\7(\2\2\u013bA\3\2\2\2\u013c")
        buf.write("\u013d\5D#\2\u013d\u013e\7-\2\2\u013e\u013f\5B\"\2\u013f")
        buf.write("\u0142\3\2\2\2\u0140\u0142\5D#\2\u0141\u013c\3\2\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142C\3\2\2\2\u0143\u0144\5F$\2\u0144")
        buf.write("\u0145\7%\2\2\u0145\u0146\5F$\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0149\5F$\2\u0148\u0143\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("E\3\2\2\2\u014a\u014b\5H%\2\u014b\u014c\t\3\2\2\u014c")
        buf.write("\u014d\5H%\2\u014d\u0150\3\2\2\2\u014e\u0150\5H%\2\u014f")
        buf.write("\u014a\3\2\2\2\u014f\u014e\3\2\2\2\u0150G\3\2\2\2\u0151")
        buf.write("\u0152\b%\1\2\u0152\u0153\5J&\2\u0153\u0159\3\2\2\2\u0154")
        buf.write("\u0155\f\4\2\2\u0155\u0156\t\4\2\2\u0156\u0158\5J&\2\u0157")
        buf.write("\u0154\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015aI\3\2\2\2\u015b\u0159\3\2\2")
        buf.write("\2\u015c\u015d\b&\1\2\u015d\u015e\5L\'\2\u015e\u0164\3")
        buf.write("\2\2\2\u015f\u0160\f\4\2\2\u0160\u0161\t\5\2\2\u0161\u0163")
        buf.write("\5L\'\2\u0162\u015f\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165K\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0167\u0168\b\'\1\2\u0168\u0169\5N(\2\u0169")
        buf.write("\u016f\3\2\2\2\u016a\u016b\f\4\2\2\u016b\u016c\t\6\2\2")
        buf.write("\u016c\u016e\5N(\2\u016d\u016a\3\2\2\2\u016e\u0171\3\2")
        buf.write("\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170M\3")
        buf.write("\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\7\33\2\2\u0173")
        buf.write("\u0176\5N(\2\u0174\u0176\5P)\2\u0175\u0172\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176O\3\2\2\2\u0177\u0178\t\5\2\2\u0178")
        buf.write("\u017b\5P)\2\u0179\u017b\5R*\2\u017a\u0177\3\2\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017bQ\3\2\2\2\u017c\u0184\7.\2\2\u017d")
        buf.write("\u017e\7.\2\2\u017e\u0180\7\'\2\2\u017f\u0181\5B\"\2\u0180")
        buf.write("\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\7(\2\2\u0183\u017c\3\2\2\2\u0183\u017d\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\7+\2\2\u0186\u0187")
        buf.write("\5B\"\2\u0187\u0188\7,\2\2\u0188\u018b\3\2\2\2\u0189\u018b")
        buf.write("\5T+\2\u018a\u0183\3\2\2\2\u018a\u0189\3\2\2\2\u018bS")
        buf.write("\3\2\2\2\u018c\u0194\5@!\2\u018d\u0194\7.\2\2\u018e\u0194")
        buf.write("\5<\37\2\u018f\u0190\7\'\2\2\u0190\u0191\5D#\2\u0191\u0192")
        buf.write("\7(\2\2\u0192\u0194\3\2\2\2\u0193\u018c\3\2\2\2\u0193")
        buf.write("\u018d\3\2\2\2\u0193\u018e\3\2\2\2\u0193\u018f\3\2\2\2")
        buf.write("\u0194U\3\2\2\2\u0195\u0197\7\62\2\2\u0196\u0195\3\2\2")
        buf.write("\2\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199W\3\2\2\2._chmz~\u0084\u0091\u0097\u009b")
        buf.write("\u009f\u00a3\u00aa\u00b2\u00b6\u00ba\u00bf\u00ca\u00cf")
        buf.write("\u00da\u00e6\u00ec\u00ef\u00f6\u00fc\u0105\u0111\u0118")
        buf.write("\u0128\u012f\u0138\u0141\u0148\u014f\u0159\u0164\u016f")
        buf.write("\u0175\u017a\u0180\u0183\u018a\u0193\u0198")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'bool'", "'string'", 
                     "'number'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "BOOL", "STRING", "NUMBER", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", 
                      "AND", "OR", "EQ", "ASSIGN", "NOT_EQ", "LT", "LTE", 
                      "GT", "GTE", "ELLIPSIS", "EQ_EQ", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", 
                      "ID", "NUMBER_LIT", "BOOL_LIT", "STRING_LIT", "NEWLINE", 
                      "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESC_LIT", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declist = 1
    RULE_declared = 2
    RULE_vardecl = 3
    RULE_vardecl_1 = 4
    RULE_vardecl_2 = 5
    RULE_vardecl_3 = 6
    RULE_typ_lit = 7
    RULE_arraydecl = 8
    RULE_numberlist = 9
    RULE_funcdecl = 10
    RULE_parameter_list = 11
    RULE_parameter = 12
    RULE_statement_list = 13
    RULE_statement_prime = 14
    RULE_statement = 15
    RULE_declaration_statement = 16
    RULE_assignment_statement = 17
    RULE_lhs = 18
    RULE_array_lhs = 19
    RULE_if_statement = 20
    RULE_elif_list_part = 21
    RULE_for_statement = 22
    RULE_break_statement = 23
    RULE_continue_statement = 24
    RULE_return_statement = 25
    RULE_call_statement = 26
    RULE_block_statement = 27
    RULE_list_literal = 28
    RULE_literal = 29
    RULE_array_literal = 30
    RULE_funcall = 31
    RULE_explist = 32
    RULE_expression = 33
    RULE_exp1 = 34
    RULE_exp2 = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_exp5 = 38
    RULE_exp6 = 39
    RULE_exp7 = 40
    RULE_exp8 = 41
    RULE_ignore = 42

    ruleNames =  [ "program", "declist", "declared", "vardecl", "vardecl_1", 
                   "vardecl_2", "vardecl_3", "typ_lit", "arraydecl", "numberlist", 
                   "funcdecl", "parameter_list", "parameter", "statement_list", 
                   "statement_prime", "statement", "declaration_statement", 
                   "assignment_statement", "lhs", "array_lhs", "if_statement", 
                   "elif_list_part", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "block_statement", "list_literal", "literal", "array_literal", 
                   "funcall", "explist", "expression", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    BOOL=3
    STRING=4
    NUMBER=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    PLUS=20
    MINUS=21
    MUL=22
    DIV=23
    MOD=24
    NOT=25
    AND=26
    OR=27
    EQ=28
    ASSIGN=29
    NOT_EQ=30
    LT=31
    LTE=32
    GT=33
    GTE=34
    ELLIPSIS=35
    EQ_EQ=36
    LPAREN=37
    RPAREN=38
    LBRACE=39
    RBRACE=40
    LBRACKET=41
    RBRACKET=42
    COMMA=43
    ID=44
    NUMBER_LIT=45
    BOOL_LIT=46
    STRING_LIT=47
    NEWLINE=48
    COMMENT=49
    WS=50
    ERROR_CHAR=51
    UNCLOSE_STRING=52
    ILLEGAL_ESC_LIT=53
    ILLEGAL_ESCAPE=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declist(self):
            return self.getTypedRuleContext(ZCodeParser.DeclistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.declist()
            self.state = 87
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def declist(self):
            return self.getTypedRuleContext(ZCodeParser.DeclistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclist" ):
                return visitor.visitDeclist(self)
            else:
                return visitor.visitChildren(self)




    def declist(self):

        localctx = ZCodeParser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declist)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.declared()
                self.state = 90
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def vardecl_1(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_1Context,0)


        def vardecl_2(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_2Context,0)


        def vardecl_3(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.VAR]:
                    self.state = 99
                    self.vardecl_1()
                    pass
                elif token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER]:
                    self.state = 100
                    self.vardecl_2()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 101
                    self.vardecl_3()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 104
                self.ignore()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_1" ):
                return visitor.visitVardecl_1(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_1(self):

        localctx = ZCodeParser.Vardecl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZCodeParser.VAR)
            self.state = 110
            self.match(ZCodeParser.ID)
            self.state = 111
            self.match(ZCodeParser.ASSIGN)
            self.state = 112
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Typ_litContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def numberlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumberlistContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_2" ):
                return visitor.visitVardecl_2(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_2(self):

        localctx = ZCodeParser.Vardecl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.typ_lit()
            self.state = 115
            self.match(ZCodeParser.ID)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 116
                self.match(ZCodeParser.LBRACKET)
                self.state = 117
                self.numberlist()
                self.state = 118
                self.match(ZCodeParser.RBRACKET)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 122
                self.match(ZCodeParser.ASSIGN)
                self.state = 123
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_3" ):
                return visitor.visitVardecl_3(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_3(self):

        localctx = ZCodeParser.Vardecl_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl_3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(ZCodeParser.DYNAMIC)
            self.state = 127
            self.match(ZCodeParser.ID)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 128
                self.match(ZCodeParser.ASSIGN)
                self.state = 129
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typ_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp_lit" ):
                return visitor.visitTyp_lit(self)
            else:
                return visitor.visitChildren(self)




    def typ_lit(self):

        localctx = ZCodeParser.Typ_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typ_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.NUMBER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def numberlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumberlistContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ZCodeParser.ID)
            self.state = 135
            self.match(ZCodeParser.LBRACKET)
            self.state = 136
            self.numberlist()
            self.state = 137
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numberlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumberlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberlist" ):
                return visitor.visitNumberlist(self)
            else:
                return visitor.visitChildren(self)




    def numberlist(self):

        localctx = ZCodeParser.NumberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numberlist)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 140
                self.match(ZCodeParser.COMMA)
                self.state = 141
                self.numberlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(ZCodeParser.FUNC)
            self.state = 146
            self.match(ZCodeParser.ID)
            self.state = 147
            self.match(ZCodeParser.LPAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.NUMBER))) != 0):
                self.state = 148
                self.parameter_list()


            self.state = 151
            self.match(ZCodeParser.RPAREN)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 152
                    self.ignore()


                self.state = 155
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 156
                    self.ignore()


                self.state = 159
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 160
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_list)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.parameter()
                self.state = 164
                self.match(ZCodeParser.COMMA)
                self.state = 165
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Typ_litContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def numberlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumberlistContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.typ_lit()
            self.state = 171
            self.match(ZCodeParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 172
                self.match(ZCodeParser.LBRACKET)
                self.state = 173
                self.numberlist()
                self.state = 174
                self.match(ZCodeParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement_list)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.statement_prime()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_primeContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_prime" ):
                return visitor.visitStatement_prime(self)
            else:
                return visitor.visitChildren(self)




    def statement_prime(self):

        localctx = ZCodeParser.Statement_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement_prime)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.statement()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 183
                    self.ignore()


                self.state = 186
                self.statement_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 197
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 198
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 199
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def vardecl_1(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_1Context,0)


        def vardecl_2(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_2Context,0)


        def vardecl_3(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.state = 202
                self.vardecl_1()
                pass
            elif token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER]:
                self.state = 203
                self.vardecl_2()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 204
                self.vardecl_3()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 207
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.lhs()
            self.state = 210
            self.match(ZCodeParser.ASSIGN)
            self.state = 211
            self.expression()
            self.state = 212
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lhs(self):
            return self.getTypedRuleContext(ZCodeParser.Array_lhsContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.array_lhs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(ZCodeParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lhs" ):
                return visitor.visitArray_lhs(self)
            else:
                return visitor.visitChildren(self)




    def array_lhs(self):

        localctx = ZCodeParser.Array_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ZCodeParser.ID)
            self.state = 219
            self.match(ZCodeParser.LBRACKET)
            self.state = 220
            self.explist()
            self.state = 221
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def elif_list_part(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_list_partContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ZCodeParser.IF)
            self.state = 224
            self.match(ZCodeParser.LPAREN)
            self.state = 225
            self.expression()
            self.state = 226
            self.match(ZCodeParser.RPAREN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 227
                self.ignore()


            self.state = 230
            self.statement()
            self.state = 231
            self.elif_list_part()
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 232
                self.match(ZCodeParser.ELSE)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 233
                    self.ignore()


                self.state = 236
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_list_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_list_part(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_list_partContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list_part" ):
                return visitor.visitElif_list_part(self)
            else:
                return visitor.visitChildren(self)




    def elif_list_part(self):

        localctx = ZCodeParser.Elif_list_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elif_list_part)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(ZCodeParser.ELIF)
                self.state = 240
                self.match(ZCodeParser.LPAREN)
                self.state = 241
                self.expression()
                self.state = 242
                self.match(ZCodeParser.RPAREN)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 243
                    self.ignore()


                self.state = 246
                self.statement()
                self.state = 247
                self.elif_list_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ZCodeParser.FOR)
            self.state = 253
            self.match(ZCodeParser.ID)
            self.state = 254
            self.match(ZCodeParser.UNTIL)
            self.state = 255
            self.expression()
            self.state = 256
            self.match(ZCodeParser.BY)
            self.state = 257
            self.expression()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 258
                self.ignore()


            self.state = 261
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ZCodeParser.BREAK)
            self.state = 264
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.CONTINUE)
            self.state = 267
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.RETURN)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 270
                self.expression()


            self.state = 273
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ZCodeParser.ID)
            self.state = 276
            self.match(ZCodeParser.LPAREN)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 277
                self.explist()


            self.state = 280
            self.match(ZCodeParser.RPAREN)
            self.state = 281
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ZCodeParser.BEGIN)
            self.state = 284
            self.ignore()
            self.state = 285
            self.statement_list()
            self.state = 286
            self.match(ZCodeParser.END)
            self.state = 287
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = ZCodeParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_list_literal)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.literal()
                self.state = 290
                self.match(ZCodeParser.COMMA)
                self.state = 291
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_literal)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.LBRACKET)
            self.state = 304
            self.explist()
            self.state = 305
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = ZCodeParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(ZCodeParser.ID)
            self.state = 308
            self.match(ZCodeParser.LPAREN)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 309
                self.explist()


            self.state = 312
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = ZCodeParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_explist)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.expression()
                self.state = 315
                self.match(ZCodeParser.COMMA)
                self.state = 316
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def ELLIPSIS(self):
            return self.getToken(ZCodeParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.exp1()
                self.state = 322
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 323
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def EQ_EQ(self):
            return self.getToken(ZCodeParser.EQ_EQ, 0)

        def NOT_EQ(self):
            return self.getToken(ZCodeParser.NOT_EQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.exp2(0)
                self.state = 329
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NOT_EQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.EQ_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 330
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 340
                    self.exp3(0) 
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 349
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 350
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 351
                    self.exp4(0) 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 362
                    self.exp5() 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp5)
        try:
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(ZCodeParser.NOT)
                self.state = 369
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp6)
        self._la = 0 # Token type
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.PLUS, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 374
                self.exp6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def explist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExplistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExplistContext,i)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 378
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 379
                    self.match(ZCodeParser.ID)
                    self.state = 380
                    self.match(ZCodeParser.LPAREN)
                    self.state = 382
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                        self.state = 381
                        self.explist()


                    self.state = 384
                    self.match(ZCodeParser.RPAREN)
                    pass


                self.state = 387
                self.match(ZCodeParser.LBRACKET)
                self.state = 388
                self.explist()
                self.state = 389
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp8)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.funcall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.match(ZCodeParser.LPAREN)
                self.state = 398
                self.expression()
                self.state = 399
                self.match(ZCodeParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 403
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 406 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.exp2_sempred
        self._predicates[36] = self.exp3_sempred
        self._predicates[37] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




