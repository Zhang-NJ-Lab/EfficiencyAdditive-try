from chemdataextractor.doc import Document
#from chemdataextractor.doc.document
from chemdataextractor.model.units import TemperatureModel, RatioModel,TimeModel,DimensionlessModel
from chemdataextractor.model.model import Compound, ModelType, StringType, CurieTemperature
from chemdataextractor.model.base import BaseModel
#from chemdataextractor.model.pv_model import OpenCircuitVoltage
from chemdataextractor.parse.elements import I,R,W,Optional,ZeroOrMore,Any,Start,Not
from chemdataextractor.parse.actions import join, merge
from chemdataextractor.model.pv_model import PowerConversionEfficiency, Perovskite,Additive,SentenceDye,CommonSentenceDye
from chemdataextractor.reader.plaintext import PlainTextReader
from chemdataextractor.parse.auto import AutoSentenceParserOptionalCompound, AutoSentenceParserPerovskite

#
with open('1.txt', 'rb') as f:
    doc = Document.from_file(f)

#print(doc.cems)
doc.records


class PCEandPerovskiteandAdditive(RatioModel):
    #specifier = StringType(parse_expression=(I('PCE') | I('η') | I('Ƞ') | I('eff') | I('efficiency') | I('PCES')), required=True, contextual=False, updatable=True)
    specifier = StringType(parse_expression=(I('PCE') | I('η') | I('Ƞ') | I('eff') |(I('power')+I('conversion')+I('efficiency')).add_action(join) | I('PCES')),required=True, contextual=False, updatable=True)
    additive = ModelType(Additive, required=False, contextual=False)
    perovskite = ModelType(Perovskite, required=False, contextual=False)

    parsers = [AutoSentenceParserOptionalCompound()]#改动




f = open('1.txt','rb')
doc = Document.from_file(f)

doc.models = [PCEandPerovskiteandAdditive]


print(doc.models)
for record in doc.records:
    print(record.serialize())
   #print(record.serialize(),file=a)
    f = open(r'out.txt', 'a', encoding='UTF8')
    print(record.serialize(), file=f)