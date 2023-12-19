from random import randint

alphabet = 'АБтВ:ГёДыЕeЁЖЗ(ИсЙуКgЛяМ кНCжфвОaПРнСшхТУацФtоХэЦЧ-rШчЩрЪщбюйdЫЬепЭъЮЯ)ь3иb,гзмдyл1KlsWmsaPw'
one = 'жЩЩжшЧёюоё,жзцжgжя1Ч1уЯюз1ЮюыжфяЯзё,жЯюзРоёТЖежёоТЮХжяжкЧТНb'
two = 'Ор(СЦ(пжмlжTW (ржыг'
three = 'жЩЩж)sЮфёюЧТТЖЮжфяюзsфзжrёЧжЯsЧцЧджзлЩложrёЧyЧжР1ЮgёЧжКgшохзФЮкНжРжёРЧe1жЯЧKоюфЮжЫЖsзжKЮТ,yз'
four = 'жЩЩжДЖжТо'
five = '%жЧsяцджKsНжЯЧsящЮТзНжТяaТЧyЧжРо1жgЧЧЫdЮТзНжзgЯЧs,ляеёЮжKЧщЮюТзежлоЯяgфжrёЧyЧжgфюзЯёо'
six = 'жЩЩжхолРзРоеgНж1яцёоюфоджоцоц'
seven = 'ДРЮKзёЮжРоаЮжз1Ныж'
eight = 'МофЧежёЮфgёжРЖжЯЧsящзёЮжЯюзжgsЧaЮТззжgsЧРж"Cяцёою"жзж"sЧц"?'
nine = 'CяцёоюжsЧц'
ten = 'вЮЯюоРзs,ТЧ!жшЧЯюЧЫяежЮdeжюол!'

def justprinter(message):
    print(message)

def justtroller(message):
    result = ''
    suggestions = [four, five, six]
    for x in range(len(message)):
        for i in suggestions[x]:
            position = alphabet.find(i)    
            new_position = position - (3 + 2 - 2 - 4 + 5)
            if i in alphabet:
                result += alphabet[new_position]
            else:
                result += i
        if x == 0:
            result += ' ' + str(randint(1, 100))

    print(f'{result}')
    ihateniggeSS(six)

def chinanumberone(message):
    try:
        result = ''
        for i in message:
            position = alphabet.find(i)
            new_position = position + (3 + 2 - 2 - 4 + 5)
            if i in alphabet:
                result += alphabet[new_position]
            else:
                result += i
    except:
        pass
    justtroller('qq')

def ihateniggeSS(message):
    result = ''
    for i in message:
        position = alphabet.find(i)    
        new_position = position - (3 + 2 - 2 - 4 + 5)
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i
    justprinter(result)

def getresult(message):
    result = ''
    for i in message:
        position = alphabet.find(i)    
        new_position = position - (3 + 2 - 2 - 4 + 5)
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i
    return result

if __name__ == '__main__':
    text = getresult(seven)
    text = input(f'{text}')
    chinanumberone('TOPSECRET')

def start():
    damn = getresult(eight)
    sheet = getresult(nine)
    pump = getresult(ten)
    while True:
        if input(f'{damn}  -> ') == sheet and __name__ != '__main__':
            break
        else:
            print(pump)

    suggestions = [three, one, two]
    for i in range(len(suggestions)):
        if i == 2:
            print(f'\n')
        ihateniggeSS(suggestions[i])