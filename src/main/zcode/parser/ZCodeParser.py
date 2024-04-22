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
        buf.write("\u0199\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\3\4\5\4e\n\4\3\5\3\5\3")
        buf.write("\5\5\5j\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7y\n\7\3\7\3\7\5\7}\n\7\3\b\3\b\3\b\3\b\5")
        buf.write("\b\u0083\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u0090\n\13\3\f\3\f\3\f\3\f\5\f\u0096\n\f\3")
        buf.write("\f\3\f\5\f\u009a\n\f\3\f\3\f\5\f\u009e\n\f\3\f\3\f\5\f")
        buf.write("\u00a2\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00a9\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00b1\n\16\3\17\3\17\5\17\u00b5")
        buf.write("\n\17\3\20\3\20\5\20\u00b9\n\20\3\20\3\20\3\20\5\20\u00be")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00c9\n\21\3\22\3\22\3\22\5\22\u00ce\n\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u00d9\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u00e5")
        buf.write("\n\26\3\26\3\26\3\26\3\26\5\26\u00eb\n\26\3\26\5\26\u00ee")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u00f5\n\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00fb\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0104\n\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\33\3\33\5\33\u0110\n\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\5\34\u0117\n\34\3\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u0127")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u012e\n\37\3 \3 \3")
        buf.write(" \3 \3!\3!\3!\5!\u0137\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u0140\n\"\3#\3#\3#\3#\3#\5#\u0147\n#\3$\3$\3$\3$\3")
        buf.write("$\5$\u014e\n$\3%\3%\3%\3%\3%\3%\7%\u0156\n%\f%\16%\u0159")
        buf.write("\13%\3&\3&\3&\3&\3&\3&\7&\u0161\n&\f&\16&\u0164\13&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\7\'\u016c\n\'\f\'\16\'\u016f\13")
        buf.write("\'\3(\3(\3(\5(\u0174\n(\3)\3)\3)\5)\u0179\n)\3*\3*\3*")
        buf.write("\3*\5*\u017f\n*\3*\5*\u0182\n*\3*\3*\3*\3*\3*\5*\u0189")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\3+\5+\u0192\n+\3,\6,\u0195\n,\r")
        buf.write(",\16,\u0196\3,\2\5HJL-\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\7\3\2\5")
        buf.write("\7\5\2\36\36 $&&\3\2\34\35\3\2\26\27\3\2\30\32\2\u01a8")
        buf.write("\2X\3\2\2\2\4_\3\2\2\2\6d\3\2\2\2\bi\3\2\2\2\nm\3\2\2")
        buf.write("\2\fr\3\2\2\2\16~\3\2\2\2\20\u0084\3\2\2\2\22\u0086\3")
        buf.write("\2\2\2\24\u008f\3\2\2\2\26\u0091\3\2\2\2\30\u00a8\3\2")
        buf.write("\2\2\32\u00aa\3\2\2\2\34\u00b4\3\2\2\2\36\u00bd\3\2\2")
        buf.write("\2 \u00c8\3\2\2\2\"\u00cd\3\2\2\2$\u00d1\3\2\2\2&\u00d8")
        buf.write("\3\2\2\2(\u00da\3\2\2\2*\u00df\3\2\2\2,\u00fa\3\2\2\2")
        buf.write(".\u00fc\3\2\2\2\60\u0107\3\2\2\2\62\u010a\3\2\2\2\64\u010d")
        buf.write("\3\2\2\2\66\u0113\3\2\2\28\u011b\3\2\2\2:\u0126\3\2\2")
        buf.write("\2<\u012d\3\2\2\2>\u012f\3\2\2\2@\u0133\3\2\2\2B\u013f")
        buf.write("\3\2\2\2D\u0146\3\2\2\2F\u014d\3\2\2\2H\u014f\3\2\2\2")
        buf.write("J\u015a\3\2\2\2L\u0165\3\2\2\2N\u0173\3\2\2\2P\u0178\3")
        buf.write("\2\2\2R\u0188\3\2\2\2T\u0191\3\2\2\2V\u0194\3\2\2\2XY")
        buf.write("\5\4\3\2YZ\7\2\2\3Z\3\3\2\2\2[\\\5\6\4\2\\]\5\4\3\2]`")
        buf.write("\3\2\2\2^`\5\6\4\2_[\3\2\2\2_^\3\2\2\2`\5\3\2\2\2ae\5")
        buf.write("\b\5\2be\5\26\f\2ce\5V,\2da\3\2\2\2db\3\2\2\2dc\3\2\2")
        buf.write("\2e\7\3\2\2\2fj\5\n\6\2gj\5\f\7\2hj\5\16\b\2if\3\2\2\2")
        buf.write("ig\3\2\2\2ih\3\2\2\2jk\3\2\2\2kl\5V,\2l\t\3\2\2\2mn\7")
        buf.write("\t\2\2no\7.\2\2op\7\37\2\2pq\5D#\2q\13\3\2\2\2rs\5\20")
        buf.write("\t\2sx\7.\2\2tu\7+\2\2uv\5\24\13\2vw\7,\2\2wy\3\2\2\2")
        buf.write("xt\3\2\2\2xy\3\2\2\2y|\3\2\2\2z{\7\37\2\2{}\5D#\2|z\3")
        buf.write("\2\2\2|}\3\2\2\2}\r\3\2\2\2~\177\7\n\2\2\177\u0082\7.")
        buf.write("\2\2\u0080\u0081\7\37\2\2\u0081\u0083\5D#\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085")
        buf.write("\t\2\2\2\u0085\21\3\2\2\2\u0086\u0087\7.\2\2\u0087\u0088")
        buf.write("\7+\2\2\u0088\u0089\5\24\13\2\u0089\u008a\7,\2\2\u008a")
        buf.write("\23\3\2\2\2\u008b\u008c\7/\2\2\u008c\u008d\7-\2\2\u008d")
        buf.write("\u0090\5\24\13\2\u008e\u0090\7/\2\2\u008f\u008b\3\2\2")
        buf.write("\2\u008f\u008e\3\2\2\2\u0090\25\3\2\2\2\u0091\u0092\7")
        buf.write("\13\2\2\u0092\u0093\7.\2\2\u0093\u0095\7\'\2\2\u0094\u0096")
        buf.write("\5\30\r\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u00a1\7(\2\2\u0098\u009a\5V,\2\u0099")
        buf.write("\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u00a2\5\64\33\2\u009c\u009e\5V,\2\u009d\u009c\3")
        buf.write("\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a2")
        buf.write("\58\35\2\u00a0\u00a2\5V,\2\u00a1\u0099\3\2\2\2\u00a1\u009d")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\27\3\2\2\2\u00a3\u00a4")
        buf.write("\5\32\16\2\u00a4\u00a5\7-\2\2\u00a5\u00a6\5\30\r\2\u00a6")
        buf.write("\u00a9\3\2\2\2\u00a7\u00a9\5\32\16\2\u00a8\u00a3\3\2\2")
        buf.write("\2\u00a8\u00a7\3\2\2\2\u00a9\31\3\2\2\2\u00aa\u00ab\5")
        buf.write("\20\t\2\u00ab\u00b0\7.\2\2\u00ac\u00ad\7+\2\2\u00ad\u00ae")
        buf.write("\5\24\13\2\u00ae\u00af\7,\2\2\u00af\u00b1\3\2\2\2\u00b0")
        buf.write("\u00ac\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\33\3\2\2\2\u00b2")
        buf.write("\u00b5\5\36\20\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2\3\2\2")
        buf.write("\2\u00b4\u00b3\3\2\2\2\u00b5\35\3\2\2\2\u00b6\u00b8\5")
        buf.write(" \21\2\u00b7\u00b9\5V,\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\5\36\20\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00be\5 \21\2\u00bd\u00b6\3\2\2\2")
        buf.write("\u00bd\u00bc\3\2\2\2\u00be\37\3\2\2\2\u00bf\u00c9\5\"")
        buf.write("\22\2\u00c0\u00c9\5$\23\2\u00c1\u00c9\5*\26\2\u00c2\u00c9")
        buf.write("\5.\30\2\u00c3\u00c9\5\60\31\2\u00c4\u00c9\5\62\32\2\u00c5")
        buf.write("\u00c9\5\64\33\2\u00c6\u00c9\5\66\34\2\u00c7\u00c9\58")
        buf.write("\35\2\u00c8\u00bf\3\2\2\2\u00c8\u00c0\3\2\2\2\u00c8\u00c1")
        buf.write("\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c8")
        buf.write("\u00c4\3\2\2\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c7\3\2\2\2\u00c9!\3\2\2\2\u00ca\u00ce\5\n\6")
        buf.write("\2\u00cb\u00ce\5\f\7\2\u00cc\u00ce\5\16\b\2\u00cd\u00ca")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d0\5V,\2\u00d0#\3\2\2\2\u00d1")
        buf.write("\u00d2\5&\24\2\u00d2\u00d3\7\37\2\2\u00d3\u00d4\5D#\2")
        buf.write("\u00d4\u00d5\5V,\2\u00d5%\3\2\2\2\u00d6\u00d9\5(\25\2")
        buf.write("\u00d7\u00d9\7.\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\'\3\2\2\2\u00da\u00db\7.\2\2\u00db\u00dc")
        buf.write("\7+\2\2\u00dc\u00dd\5B\"\2\u00dd\u00de\7,\2\2\u00de)\3")
        buf.write("\2\2\2\u00df\u00e0\7\21\2\2\u00e0\u00e1\7\'\2\2\u00e1")
        buf.write("\u00e2\5D#\2\u00e2\u00e4\7(\2\2\u00e3\u00e5\5V,\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6\u00e7\5 \21\2\u00e7\u00ed\5,\27\2\u00e8\u00ea\7")
        buf.write("\22\2\2\u00e9\u00eb\5V,\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\5 \21\2\u00ed")
        buf.write("\u00e8\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee+\3\2\2\2\u00ef")
        buf.write("\u00f0\7\23\2\2\u00f0\u00f1\7\'\2\2\u00f1\u00f2\5D#\2")
        buf.write("\u00f2\u00f4\7(\2\2\u00f3\u00f5\5V,\2\u00f4\u00f3\3\2")
        buf.write("\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write("\5 \21\2\u00f7\u00f8\5,\27\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00fb\3\2\2\2\u00fa\u00ef\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb-\3\2\2\2\u00fc\u00fd\7\f\2\2\u00fd\u00fe\7.\2\2")
        buf.write("\u00fe\u00ff\7\r\2\2\u00ff\u0100\5D#\2\u0100\u0101\7\16")
        buf.write("\2\2\u0101\u0103\5D#\2\u0102\u0104\5V,\2\u0103\u0102\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106")
        buf.write("\5 \21\2\u0106/\3\2\2\2\u0107\u0108\7\17\2\2\u0108\u0109")
        buf.write("\5V,\2\u0109\61\3\2\2\2\u010a\u010b\7\20\2\2\u010b\u010c")
        buf.write("\5V,\2\u010c\63\3\2\2\2\u010d\u010f\7\b\2\2\u010e\u0110")
        buf.write("\5D#\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0112\5V,\2\u0112\65\3\2\2\2\u0113\u0114")
        buf.write("\7.\2\2\u0114\u0116\7\'\2\2\u0115\u0117\5B\"\2\u0116\u0115")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u0119\7(\2\2\u0119\u011a\5V,\2\u011a\67\3\2\2\2\u011b")
        buf.write("\u011c\7\24\2\2\u011c\u011d\5V,\2\u011d\u011e\5\34\17")
        buf.write("\2\u011e\u011f\7\25\2\2\u011f\u0120\5V,\2\u01209\3\2\2")
        buf.write("\2\u0121\u0122\5<\37\2\u0122\u0123\7-\2\2\u0123\u0124")
        buf.write("\5:\36\2\u0124\u0127\3\2\2\2\u0125\u0127\5<\37\2\u0126")
        buf.write("\u0121\3\2\2\2\u0126\u0125\3\2\2\2\u0127;\3\2\2\2\u0128")
        buf.write("\u012e\7/\2\2\u0129\u012e\7\61\2\2\u012a\u012e\7\3\2\2")
        buf.write("\u012b\u012e\7\4\2\2\u012c\u012e\5> \2\u012d\u0128\3\2")
        buf.write("\2\2\u012d\u0129\3\2\2\2\u012d\u012a\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012e=\3\2\2\2\u012f\u0130")
        buf.write("\7+\2\2\u0130\u0131\5B\"\2\u0131\u0132\7,\2\2\u0132?\3")
        buf.write("\2\2\2\u0133\u0134\7.\2\2\u0134\u0136\7\'\2\2\u0135\u0137")
        buf.write("\5B\"\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u0139\7(\2\2\u0139A\3\2\2\2\u013a")
        buf.write("\u013b\5D#\2\u013b\u013c\7-\2\2\u013c\u013d\5B\"\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u0140\5D#\2\u013f\u013a\3\2\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140C\3\2\2\2\u0141\u0142\5F$\2\u0142")
        buf.write("\u0143\7%\2\2\u0143\u0144\5F$\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0147\5F$\2\u0146\u0141\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("E\3\2\2\2\u0148\u0149\5H%\2\u0149\u014a\t\3\2\2\u014a")
        buf.write("\u014b\5H%\2\u014b\u014e\3\2\2\2\u014c\u014e\5H%\2\u014d")
        buf.write("\u0148\3\2\2\2\u014d\u014c\3\2\2\2\u014eG\3\2\2\2\u014f")
        buf.write("\u0150\b%\1\2\u0150\u0151\5J&\2\u0151\u0157\3\2\2\2\u0152")
        buf.write("\u0153\f\4\2\2\u0153\u0154\t\4\2\2\u0154\u0156\5J&\2\u0155")
        buf.write("\u0152\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158I\3\2\2\2\u0159\u0157\3\2\2")
        buf.write("\2\u015a\u015b\b&\1\2\u015b\u015c\5L\'\2\u015c\u0162\3")
        buf.write("\2\2\2\u015d\u015e\f\4\2\2\u015e\u015f\t\5\2\2\u015f\u0161")
        buf.write("\5L\'\2\u0160\u015d\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163K\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0166\b\'\1\2\u0166\u0167\5N(\2\u0167")
        buf.write("\u016d\3\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a\t\6\2\2")
        buf.write("\u016a\u016c\5N(\2\u016b\u0168\3\2\2\2\u016c\u016f\3\2")
        buf.write("\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016eM\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7\33\2\2\u0171")
        buf.write("\u0174\5N(\2\u0172\u0174\5P)\2\u0173\u0170\3\2\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174O\3\2\2\2\u0175\u0176\t\5\2\2\u0176")
        buf.write("\u0179\5P)\2\u0177\u0179\5R*\2\u0178\u0175\3\2\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179Q\3\2\2\2\u017a\u0182\7.\2\2\u017b")
        buf.write("\u017c\7.\2\2\u017c\u017e\7\'\2\2\u017d\u017f\5B\"\2\u017e")
        buf.write("\u017d\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u0182\7(\2\2\u0181\u017a\3\2\2\2\u0181\u017b\3")
        buf.write("\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\7+\2\2\u0184\u0185")
        buf.write("\5B\"\2\u0185\u0186\7,\2\2\u0186\u0189\3\2\2\2\u0187\u0189")
        buf.write("\5T+\2\u0188\u0181\3\2\2\2\u0188\u0187\3\2\2\2\u0189S")
        buf.write("\3\2\2\2\u018a\u0192\5@!\2\u018b\u0192\7.\2\2\u018c\u0192")
        buf.write("\5<\37\2\u018d\u018e\7\'\2\2\u018e\u018f\5D#\2\u018f\u0190")
        buf.write("\7(\2\2\u0190\u0192\3\2\2\2\u0191\u018a\3\2\2\2\u0191")
        buf.write("\u018b\3\2\2\2\u0191\u018c\3\2\2\2\u0191\u018d\3\2\2\2")
        buf.write("\u0192U\3\2\2\2\u0193\u0195\7\62\2\2\u0194\u0193\3\2\2")
        buf.write("\2\u0195\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197W\3\2\2\2-_dix|\u0082\u008f\u0095\u0099")
        buf.write("\u009d\u00a1\u00a8\u00b0\u00b4\u00b8\u00bd\u00c8\u00cd")
        buf.write("\u00d8\u00e4\u00ea\u00ed\u00f4\u00fa\u0103\u010f\u0116")
        buf.write("\u0126\u012d\u0136\u013f\u0146\u014d\u0157\u0162\u016d")
        buf.write("\u0173\u0178\u017e\u0181\u0188\u0191\u0196")
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
                     "']'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

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


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.funcdecl()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
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
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.state = 100
                self.vardecl_1()
                pass
            elif token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER]:
                self.state = 101
                self.vardecl_2()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 102
                self.vardecl_3()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 105
            self.ignore()
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
            self.state = 107
            self.match(ZCodeParser.VAR)
            self.state = 108
            self.match(ZCodeParser.ID)
            self.state = 109
            self.match(ZCodeParser.ASSIGN)
            self.state = 110
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
            self.state = 112
            self.typ_lit()
            self.state = 113
            self.match(ZCodeParser.ID)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 114
                self.match(ZCodeParser.LBRACKET)
                self.state = 115
                self.numberlist()
                self.state = 116
                self.match(ZCodeParser.RBRACKET)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 120
                self.match(ZCodeParser.ASSIGN)
                self.state = 121
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
            self.state = 124
            self.match(ZCodeParser.DYNAMIC)
            self.state = 125
            self.match(ZCodeParser.ID)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 126
                self.match(ZCodeParser.ASSIGN)
                self.state = 127
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
            self.state = 130
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
            self.state = 132
            self.match(ZCodeParser.ID)
            self.state = 133
            self.match(ZCodeParser.LBRACKET)
            self.state = 134
            self.numberlist()
            self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 138
                self.match(ZCodeParser.COMMA)
                self.state = 139
                self.numberlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
            self.state = 143
            self.match(ZCodeParser.FUNC)
            self.state = 144
            self.match(ZCodeParser.ID)
            self.state = 145
            self.match(ZCodeParser.LPAREN)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.NUMBER))) != 0):
                self.state = 146
                self.parameter_list()


            self.state = 149
            self.match(ZCodeParser.RPAREN)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 150
                    self.ignore()


                self.state = 153
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 154
                    self.ignore()


                self.state = 157
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 158
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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.parameter()
                self.state = 162
                self.match(ZCodeParser.COMMA)
                self.state = 163
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
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
            self.state = 168
            self.typ_lit()
            self.state = 169
            self.match(ZCodeParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 170
                self.match(ZCodeParser.LBRACKET)
                self.state = 171
                self.numberlist()
                self.state = 172
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
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.statement()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 181
                    self.ignore()


                self.state = 184
                self.statement_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 193
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 194
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 195
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 196
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 197
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
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.state = 200
                self.vardecl_1()
                pass
            elif token in [ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.NUMBER]:
                self.state = 201
                self.vardecl_2()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 202
                self.vardecl_3()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
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
            self.state = 207
            self.lhs()
            self.state = 208
            self.match(ZCodeParser.ASSIGN)
            self.state = 209
            self.expression()
            self.state = 210
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
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.array_lhs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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
            self.state = 216
            self.match(ZCodeParser.ID)
            self.state = 217
            self.match(ZCodeParser.LBRACKET)
            self.state = 218
            self.explist()
            self.state = 219
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
            self.state = 221
            self.match(ZCodeParser.IF)
            self.state = 222
            self.match(ZCodeParser.LPAREN)
            self.state = 223
            self.expression()
            self.state = 224
            self.match(ZCodeParser.RPAREN)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 225
                self.ignore()


            self.state = 228
            self.statement()
            self.state = 229
            self.elif_list_part()
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(ZCodeParser.ELSE)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 231
                    self.ignore()


                self.state = 234
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
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.ELIF)
                self.state = 238
                self.match(ZCodeParser.LPAREN)
                self.state = 239
                self.expression()
                self.state = 240
                self.match(ZCodeParser.RPAREN)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 241
                    self.ignore()


                self.state = 244
                self.statement()
                self.state = 245
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
            self.state = 250
            self.match(ZCodeParser.FOR)
            self.state = 251
            self.match(ZCodeParser.ID)
            self.state = 252
            self.match(ZCodeParser.UNTIL)
            self.state = 253
            self.expression()
            self.state = 254
            self.match(ZCodeParser.BY)
            self.state = 255
            self.expression()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 256
                self.ignore()


            self.state = 259
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
            self.state = 261
            self.match(ZCodeParser.BREAK)
            self.state = 262
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
            self.state = 264
            self.match(ZCodeParser.CONTINUE)
            self.state = 265
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
            self.state = 267
            self.match(ZCodeParser.RETURN)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 268
                self.expression()


            self.state = 271
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
            self.state = 273
            self.match(ZCodeParser.ID)
            self.state = 274
            self.match(ZCodeParser.LPAREN)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 275
                self.explist()


            self.state = 278
            self.match(ZCodeParser.RPAREN)
            self.state = 279
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
            self.state = 281
            self.match(ZCodeParser.BEGIN)
            self.state = 282
            self.ignore()
            self.state = 283
            self.statement_list()
            self.state = 284
            self.match(ZCodeParser.END)
            self.state = 285
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
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.literal()
                self.state = 288
                self.match(ZCodeParser.COMMA)
                self.state = 289
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 298
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
            self.state = 301
            self.match(ZCodeParser.LBRACKET)
            self.state = 302
            self.explist()
            self.state = 303
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
            self.state = 305
            self.match(ZCodeParser.ID)
            self.state = 306
            self.match(ZCodeParser.LPAREN)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 307
                self.explist()


            self.state = 310
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
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.expression()
                self.state = 313
                self.match(ZCodeParser.COMMA)
                self.state = 314
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.exp1()
                self.state = 320
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 321
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
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
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.exp2(0)
                self.state = 327
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NOT_EQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.EQ_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 328
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
            self.state = 334
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 336
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 337
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 338
                    self.exp3(0) 
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 345
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 349
                    self.exp4(0) 
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
            self.state = 356
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 360
                    self.exp5() 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(ZCodeParser.NOT)
                self.state = 367
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.PLUS, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 372
                self.exp6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
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
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 376
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 377
                    self.match(ZCodeParser.ID)
                    self.state = 378
                    self.match(ZCodeParser.LPAREN)
                    self.state = 380
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                        self.state = 379
                        self.explist()


                    self.state = 382
                    self.match(ZCodeParser.RPAREN)
                    pass


                self.state = 385
                self.match(ZCodeParser.LBRACKET)
                self.state = 386
                self.explist()
                self.state = 387
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.funcall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.match(ZCodeParser.LPAREN)
                self.state = 396
                self.expression()
                self.state = 397
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
            self.state = 402 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 401
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 404 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
         




