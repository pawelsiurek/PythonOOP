from modules.dog import Dog
from modules.golden_retriever import GoldenRetriever
from modules.chihuahua import Chihuahua

g_r1 = GoldenRetriever("Tequila", 7)
szczurek = Chihuahua("Fafik", 2)

print(g_r1.bark())
print(szczurek.bark())