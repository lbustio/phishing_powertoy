#from mpmath.functions.functions import root
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from utils import *
from config import *

persuasive_words_dict = { "ahora": "Urgencia", "ya": "Urgencia", "date prisa": "Urgencia", "rápido": "Urgencia", "hoy": "Urgencia",
                   "de inmediato": "Urgencia", "directo": "Urgencia", "nuevo": "Urgencia", "lo último": "Urgencia", "urgente": "Urgencia",
                   "solo": "Urgencia", "descubrir": "Urgencia", "aprovechar": "Urgencia", "adelantarse": "Urgencia", "acción": "Urgencia", "instante": "Urgencia",
                   "segundos": "Urgencia", "minutos": "Urgencia", "horas": "Urgencia",
                   #cause-and-effect words and phrases
                   "exclusivo": "exclusividad", "único": "exclusividad", "especial": "exclusividad",
                   "el primero": "exclusividad", "solo para": "exclusividad", "sé uno de los": "exclusividad",
                   "auténtico": "exclusividad", "limitado": "exclusividad", "secreto": "exclusividad", "verdad": "exclusividad", "cima": "exclusividad",
                   #words and phrases that make you feel safe
                    "limitado": "escasez", "final": "escasez", "solo disponible aquí": "escasez", "solo para": "escasez", "definitivo": "escasez",
                    "termina en": "escasez", "exprés": "escasez",
                   #ubiquitous power words
                   "ahorrar": "ahorro", "ganar": "ahorro", "ahorro": "ahorro", "gratis": "ahorro", "económico": "ahorro", "reducido": "ahorro",
                   "reducir": "ahorro", "en menos tiempo": "ahorro", "descuento": "ahorro", "bono": "ahorro", "promoción": "ahorro",
                   "oferta": "ahorro", "rebaja": "ahorro", "precios bajos": "ahorro", "básico": "ahorro", "recuperar": "ahorro", "devolver": "ahorro",
                    "reembolso": "ahorro","recompensa": "ahorro",
                   #word for shareable content
                   "garantizar": "confianza", "garantía": "confianza", "probar": "confianza", "fácil": "confianza", "sencillo": "confianza", "simple": "confianza",
                    "cuidar": "confianza", "cuidado": "confianza", "asegurar": "confianza", "seguro": "confianza", "seguridad": "confianza", "proteger": "confianza",
                    "protección": "confianza", "de toda la vida": "confianza", "certificar": "confianza", "acreditar": "confianza", "avalar": "confianza", "auténtico": "confianza",
                    "genuino": "confianza", "a tu ritmo": "confianza", "desde el primer día": "confianza", "sin riesgos": "confianza", "sin compromiso": "confianza",
                    "sin comisiones": "confianza", "resultado": "confianza", "devolver": "confianza", "paso a paso": "confianza", "anunciado en": "confianza",
                    "más vendido": "confianza", "profesional": "confianza", "privado": "confianza", "autoridad reconocida": "confianza", "legal": "confianza",
                    "nunca falla": "confianza",
                    #preocupación
                    "miedo": "preocupación", "aburrido": "preocupación", "desmotivado": "preocupación", "soledad": "preocupación", "difícil": "preocupación", "lento": "preocupación",
                    "complejo": "preocupación", "rechazo": "preocupación", "tensión": "preocupación", "esttrés": "preocupación", "responsabilidad": "preocupación", "culpa": "preocupación",
                    "preocuipación": "preocupación", "odio": "preocupación", "terror": "preocupación", "fracaso": "preocupación", "pero": "preocupación",
                    # unión - pertenencia a comunidad
                    "unión": "comunidad", "sumar": "comunidad", "compañía": "comunidad", "acompañar": "comunidad", "juntos": "comunidad",
                    "contigo": "comunidad", "amigos": "comunidad", "familia": "comunidad", "apoyo": "comunidad", "respaldo": "comunidad",
                    "ayudar": "comunidad", "ayuda": "comunidad", "los más vendidos": "comunidad", "confían": "comunidad", "registrarse": "comunidad", "suscribirse": "comunidad",
                    #curiosidad
                    "prohibir": "curiosidad", "esconder": "curiosidad", "ocultar": "curiosidad", "mentir": "curiosidad", "falso": "curiosidad",
                    "perdido": "curiosidad", "puerta trasera": "curiosidad", "lo nunca visto": "curiosidad", "proscrito": "curiosidad", "lista negra": "curiosidad",
                    "ilegal": "curiosidad", "censurar": "curiosidad", "secreto": "curiosidad", "spoiler": "curiosidad", "top secret": "curiosidad",
                    "interesante": "curiosidad", "desconocer": "curiosidad", "incógnita": "curiosidad", "mito": "curiosidad", "leyenda": "curiosidad",
                    "inusual": "curiosidad", "extraño": "curiosidad", "confesar": "curiosidad", "confidencial": "curiosidad", "olvidado": "curiosidad",
                    "retener": "curiosidad", "vetar": "curiosidad"
                   }

## cargando frases relevantes
count_equal = 0
duplicated = {}
with open(rootPath + 'models//all_kpe.txt', encoding = 'unicode_escape') as f:
  for line in f:
    kpeElements = line.split(',')

for kpe in kpeElements:
  if kpe not in persuasive_words_dict.keys():
    persuasive_words_dict[kpe] = 'kpe'
  else:
    if kpe in duplicated.keys():
      duplicated[kpe] += 1
    else:
      duplicated[kpe] = 1
    count_equal += 1

## Retorna 1 si la palabra o frase esta, en otro caso 0

from re import search
def Persuasive_Words_Detector(text, persuasiveWordsDict):
  # resultVector = []
  for key, value in persuasiveWordsDict.items():
    ps = PorterStemmer()
    stem = ps.stem(key)
    #se crea expresion regular para identificar exactamente la palabra de persuacion que se busca, evitando falso positivo cuando forma parte de otra palabra
    regEx = "(^"+ key[0] +"|[^a-z]"+ key[0] +")"+ key[1:-1] +"("+key[-1]+"[^a-z]|"+key[-1]+"$)"
    #print (regEx)
    if search(regEx, text.lower()):
        persuasiveWordsDict[key] = 1
      # resultVector.append("1")
    else:
        persuasiveWordsDict[key] = 0
      # resultVector.append("0")
  # return resultVector

## Evaluando el metodo anterior

def vectorial_representation(text):

    # txt = ""
    # Lemmatization with stopwords removal
    txt = text.split()

    ps = PorterStemmer()
    stem = ""

    for word in txt:
      words = word_tokenize(word)
      for w in words:
        stem += ps.stem(w) + " "

    Persuasive_Words_Detector(stem, persuasive_words_dict)
    return persuasive_words_dict

def Paint_Text(text, reglasCubiertas, idList):
    txt = text.split()
    ps = PorterStemmer()
    addColor = False
    tokens = []
    delimiter = " "
    for id in idList:
        regla = reglasCubiertas[id]
        listObjCond = parsear_condicion(regla["condicion"])
        for word in txt:
            words = word_tokenize(word)
            for w in words:
                wStem = ps.stem(w)
                for obj in listObjCond:
                    key = obj["variable"]
                    kStem = ps.stem(key)
                    if wStem == kStem:
                        addColor = True

            if (addColor == True) & (regla["clase"] == "1"):
                tokens.append((delimiter.join(words), "Legit Rule ID: " + str(id+1), "#008000"))
            elif (addColor == True) & (regla["clase"] == "0"):
                tokens.append((delimiter.join(words), "Phishing Rule ID: " + str(id+1), "#FF8080"))
            elif addColor == True:
                tokens.append((delimiter.join(words), "Other Rule ID: " + str(id+1), "#FFFF00"))
            else:
                tokens.append(" " + delimiter.join(words) + " ")
            addColor = False
    return tokens