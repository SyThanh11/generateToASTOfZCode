# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u018d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3,\3,\3-\3-\7-\u011f\n-\f-\16-\u0122\13-\3.\3.\7.\u0126")
        buf.write("\n.\f.\16.\u0129\13.\5.\u012b\n.\3/\3/\5/\u012f\n/\3/")
        buf.write("\6/\u0132\n/\r/\16/\u0133\3\60\6\60\u0137\n\60\r\60\16")
        buf.write("\60\u0138\3\60\5\60\u013c\n\60\3\60\5\60\u013f\n\60\3")
        buf.write("\61\3\61\5\61\u0143\n\61\3\62\3\62\3\62\3\62\5\62\u0149")
        buf.write("\n\62\3\63\3\63\3\63\3\64\3\64\7\64\u0150\n\64\f\64\16")
        buf.write("\64\u0153\13\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\7\66\u015e\n\66\f\66\16\66\u0161\13\66\3\66\3\66")
        buf.write("\3\67\6\67\u0166\n\67\r\67\16\67\u0167\3\67\3\67\38\3")
        buf.write("8\38\39\39\79\u0171\n9\f9\169\u0174\139\39\39\39\59\u0179")
        buf.write("\n9\39\39\3:\3:\3:\3:\3:\5:\u0182\n:\3;\3;\7;\u0186\n")
        buf.write(";\f;\16;\u0189\13;\3;\3;\3;\2\2<\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_/a\60")
        buf.write("c\2e\2g\61i\62k\63m\64o\65q\66s\67u8\3\2\21\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\16\17")
        buf.write("$$^^\3\2))\3\2$$\t\2))^^ddhhppttvv\3\2\f\f\4\2\f\f\16")
        buf.write("\17\5\2\n\13\16\17\"\"\3\3\f\f\5\2\16\17))^^\b\2^^ddh")
        buf.write("hppttvv\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("_\3\2\2\2\2a\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\3w\3\2\2\2\5|\3\2\2\2\7\u0082\3\2\2\2\t\u0087\3\2\2")
        buf.write("\2\13\u008e\3\2\2\2\r\u0095\3\2\2\2\17\u009c\3\2\2\2\21")
        buf.write("\u00a0\3\2\2\2\23\u00a8\3\2\2\2\25\u00ad\3\2\2\2\27\u00b1")
        buf.write("\3\2\2\2\31\u00b7\3\2\2\2\33\u00ba\3\2\2\2\35\u00c0\3")
        buf.write("\2\2\2\37\u00c9\3\2\2\2!\u00cc\3\2\2\2#\u00d1\3\2\2\2")
        buf.write("%\u00d6\3\2\2\2\'\u00dc\3\2\2\2)\u00e0\3\2\2\2+\u00e2")
        buf.write("\3\2\2\2-\u00e4\3\2\2\2/\u00e6\3\2\2\2\61\u00e8\3\2\2")
        buf.write("\2\63\u00ea\3\2\2\2\65\u00ee\3\2\2\2\67\u00f2\3\2\2\2")
        buf.write("9\u00f5\3\2\2\2;\u00f7\3\2\2\2=\u00fa\3\2\2\2?\u00fd\3")
        buf.write("\2\2\2A\u00ff\3\2\2\2C\u0102\3\2\2\2E\u0104\3\2\2\2G\u0107")
        buf.write("\3\2\2\2I\u010b\3\2\2\2K\u010e\3\2\2\2M\u0110\3\2\2\2")
        buf.write("O\u0112\3\2\2\2Q\u0114\3\2\2\2S\u0116\3\2\2\2U\u0118\3")
        buf.write("\2\2\2W\u011a\3\2\2\2Y\u011c\3\2\2\2[\u012a\3\2\2\2]\u012c")
        buf.write("\3\2\2\2_\u0136\3\2\2\2a\u0142\3\2\2\2c\u0148\3\2\2\2")
        buf.write("e\u014a\3\2\2\2g\u014d\3\2\2\2i\u0157\3\2\2\2k\u0159\3")
        buf.write("\2\2\2m\u0165\3\2\2\2o\u016b\3\2\2\2q\u016e\3\2\2\2s\u0181")
        buf.write("\3\2\2\2u\u0183\3\2\2\2wx\7v\2\2xy\7t\2\2yz\7w\2\2z{\7")
        buf.write("g\2\2{\4\3\2\2\2|}\7h\2\2}~\7c\2\2~\177\7n\2\2\177\u0080")
        buf.write("\7u\2\2\u0080\u0081\7g\2\2\u0081\6\3\2\2\2\u0082\u0083")
        buf.write("\7d\2\2\u0083\u0084\7q\2\2\u0084\u0085\7q\2\2\u0085\u0086")
        buf.write("\7n\2\2\u0086\b\3\2\2\2\u0087\u0088\7u\2\2\u0088\u0089")
        buf.write("\7v\2\2\u0089\u008a\7t\2\2\u008a\u008b\7k\2\2\u008b\u008c")
        buf.write("\7p\2\2\u008c\u008d\7i\2\2\u008d\n\3\2\2\2\u008e\u008f")
        buf.write("\7p\2\2\u008f\u0090\7w\2\2\u0090\u0091\7o\2\2\u0091\u0092")
        buf.write("\7d\2\2\u0092\u0093\7g\2\2\u0093\u0094\7t\2\2\u0094\f")
        buf.write("\3\2\2\2\u0095\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098")
        buf.write("\7v\2\2\u0098\u0099\7w\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7p\2\2\u009b\16\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7t\2\2\u009f\20\3\2\2\2\u00a0\u00a1")
        buf.write("\7f\2\2\u00a1\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7e\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\24")
        buf.write("\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\26\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\30\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9")
        buf.write("\7{\2\2\u00b9\32\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7m\2\2\u00bf\34\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7h\2\2\u00cb \3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\"")
        buf.write("\3\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7h\2\2\u00d5$\3\2\2\2\u00d6\u00d7")
        buf.write("\7d\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7p\2\2\u00db&\3\2\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df(\3")
        buf.write("\2\2\2\u00e0\u00e1\7-\2\2\u00e1*\3\2\2\2\u00e2\u00e3\7")
        buf.write("/\2\2\u00e3,\3\2\2\2\u00e4\u00e5\7,\2\2\u00e5.\3\2\2\2")
        buf.write("\u00e6\u00e7\7\61\2\2\u00e7\60\3\2\2\2\u00e8\u00e9\7\'")
        buf.write("\2\2\u00e9\62\3\2\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7")
        buf.write("q\2\2\u00ec\u00ed\7v\2\2\u00ed\64\3\2\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7f\2\2\u00f1\66")
        buf.write("\3\2\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7t\2\2\u00f48")
        buf.write("\3\2\2\2\u00f5\u00f6\7?\2\2\u00f6:\3\2\2\2\u00f7\u00f8")
        buf.write("\7>\2\2\u00f8\u00f9\7/\2\2\u00f9<\3\2\2\2\u00fa\u00fb")
        buf.write("\7#\2\2\u00fb\u00fc\7?\2\2\u00fc>\3\2\2\2\u00fd\u00fe")
        buf.write("\7>\2\2\u00fe@\3\2\2\2\u00ff\u0100\7>\2\2\u0100\u0101")
        buf.write("\7?\2\2\u0101B\3\2\2\2\u0102\u0103\7@\2\2\u0103D\3\2\2")
        buf.write("\2\u0104\u0105\7@\2\2\u0105\u0106\7?\2\2\u0106F\3\2\2")
        buf.write("\2\u0107\u0108\7\60\2\2\u0108\u0109\7\60\2\2\u0109\u010a")
        buf.write("\7\60\2\2\u010aH\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d")
        buf.write("\7?\2\2\u010dJ\3\2\2\2\u010e\u010f\7*\2\2\u010fL\3\2\2")
        buf.write("\2\u0110\u0111\7+\2\2\u0111N\3\2\2\2\u0112\u0113\7}\2")
        buf.write("\2\u0113P\3\2\2\2\u0114\u0115\7\177\2\2\u0115R\3\2\2\2")
        buf.write("\u0116\u0117\7]\2\2\u0117T\3\2\2\2\u0118\u0119\7_\2\2")
        buf.write("\u0119V\3\2\2\2\u011a\u011b\7.\2\2\u011bX\3\2\2\2\u011c")
        buf.write("\u0120\t\2\2\2\u011d\u011f\t\3\2\2\u011e\u011d\3\2\2\2")
        buf.write("\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3")
        buf.write("\2\2\2\u0121Z\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0127")
        buf.write("\7\60\2\2\u0124\u0126\t\4\2\2\u0125\u0124\3\2\2\2\u0126")
        buf.write("\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u0123\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012b\\\3\2\2\2\u012c\u012e")
        buf.write("\t\5\2\2\u012d\u012f\t\6\2\2\u012e\u012d\3\2\2\2\u012e")
        buf.write("\u012f\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u0132\t\4\2\2")
        buf.write("\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131\3")
        buf.write("\2\2\2\u0133\u0134\3\2\2\2\u0134^\3\2\2\2\u0135\u0137")
        buf.write("\t\4\2\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2")
        buf.write("\u013a\u013c\5[.\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2")
        buf.write("\2\2\u013c\u013e\3\2\2\2\u013d\u013f\5]/\2\u013e\u013d")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f`\3\2\2\2\u0140\u0143")
        buf.write("\5\3\2\2\u0141\u0143\5\5\3\2\u0142\u0140\3\2\2\2\u0142")
        buf.write("\u0141\3\2\2\2\u0143b\3\2\2\2\u0144\u0149\5e\63\2\u0145")
        buf.write("\u0149\n\7\2\2\u0146\u0147\t\b\2\2\u0147\u0149\t\t\2\2")
        buf.write("\u0148\u0144\3\2\2\2\u0148\u0145\3\2\2\2\u0148\u0146\3")
        buf.write("\2\2\2\u0149d\3\2\2\2\u014a\u014b\7^\2\2\u014b\u014c\t")
        buf.write("\n\2\2\u014cf\3\2\2\2\u014d\u0151\7$\2\2\u014e\u0150\5")
        buf.write("c\62\2\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0154\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0155\7$\2\2\u0155\u0156\b\64\2\2")
        buf.write("\u0156h\3\2\2\2\u0157\u0158\t\13\2\2\u0158j\3\2\2\2\u0159")
        buf.write("\u015a\7%\2\2\u015a\u015b\7%\2\2\u015b\u015f\3\2\2\2\u015c")
        buf.write("\u015e\n\f\2\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0162\u0163\b\66\3\2\u0163")
        buf.write("l\3\2\2\2\u0164\u0166\t\r\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169\u016a\b\67\3\2\u016an\3\2\2")
        buf.write("\2\u016b\u016c\13\2\2\2\u016c\u016d\b8\4\2\u016dp\3\2")
        buf.write("\2\2\u016e\u0172\7$\2\2\u016f\u0171\5c\62\2\u0170\u016f")
        buf.write("\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0178\3\2\2\2\u0174\u0172\3\2\2\2")
        buf.write("\u0175\u0176\7\17\2\2\u0176\u0179\7\f\2\2\u0177\u0179")
        buf.write("\t\16\2\2\u0178\u0175\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\b9\5\2\u017br\3\2\2\2\u017c")
        buf.write("\u0182\t\17\2\2\u017d\u017e\7^\2\2\u017e\u0182\n\20\2")
        buf.write("\2\u017f\u0180\7)\2\2\u0180\u0182\n\t\2\2\u0181\u017c")
        buf.write("\3\2\2\2\u0181\u017d\3\2\2\2\u0181\u017f\3\2\2\2\u0182")
        buf.write("t\3\2\2\2\u0183\u0187\7$\2\2\u0184\u0186\5c\62\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u018a\u018b\5s:\2\u018b\u018c\b;\6\2\u018cv\3\2")
        buf.write("\2\2\24\2\u0120\u0127\u012a\u012e\u0133\u0138\u013b\u013e")
        buf.write("\u0142\u0148\u0151\u015f\u0167\u0172\u0178\u0181\u0187")
        buf.write("\7\3\64\2\b\2\2\38\3\39\4\3;\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    BOOL = 3
    STRING = 4
    NUMBER = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    PLUS = 20
    MINUS = 21
    MUL = 22
    DIV = 23
    MOD = 24
    NOT = 25
    AND = 26
    OR = 27
    EQ = 28
    ASSIGN = 29
    NOT_EQ = 30
    LT = 31
    LTE = 32
    GT = 33
    GTE = 34
    ELLIPSIS = 35
    EQ_EQ = 36
    LPAREN = 37
    RPAREN = 38
    LBRACE = 39
    RBRACE = 40
    LBRACKET = 41
    RBRACKET = 42
    COMMA = 43
    ID = 44
    NUMBER_LIT = 45
    BOOL_LIT = 46
    STRING_LIT = 47
    NEWLINE = 48
    COMMENT = 49
    WS = 50
    ERROR_CHAR = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESC_LIT = 53
    ILLEGAL_ESCAPE = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'bool'", "'string'", "'number'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
            "'or'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'{'", "'}'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "BOOL", "STRING", "NUMBER", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQ", "ASSIGN", "NOT_EQ", 
            "LT", "LTE", "GT", "GTE", "ELLIPSIS", "EQ_EQ", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "ID", "NUMBER_LIT", 
            "BOOL_LIT", "STRING_LIT", "NEWLINE", "COMMENT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESC_LIT", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "BOOL", "STRING", "NUMBER", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
                  "ASSIGN", "NOT_EQ", "LT", "LTE", "GT", "GTE", "ELLIPSIS", 
                  "EQ_EQ", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                  "RBRACKET", "COMMA", "ID", "DECIMAL", "EXPONENT", "NUMBER_LIT", 
                  "BOOL_LIT", "LEGAL_LIT", "ESC_LIT", "STRING_LIT", "NEWLINE", 
                  "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESC_LIT", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.STRING_LIT_action 
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                            raise UncloseString(self.text[1:-2])
            	elif(self.text[-1] == '\n'):
            		raise UncloseString(self.text[1:-1])
            	else:
                            raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:]);        

     


