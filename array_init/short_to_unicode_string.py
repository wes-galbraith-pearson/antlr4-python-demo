import re
from parser.ArrayInitListener import ArrayInitListener
from parser.ArrayInitParser import ArrayInitParser


class ShortToUnicodeString(ArrayInitListener):
    def enterInit(self, ctx: ArrayInitParser.InitContext):
        print('"')

    def exitInit(self, ctx: ArrayInitParser.InitContext):
        print('"')

    def enterValue(self, ctx: ArrayInitParser.ValueContext):
        value = str(ctx.INT())
        if re.match(r'[0-9]+', value):
            hex_value = str(hex(int(value)))
            print(hex_value)