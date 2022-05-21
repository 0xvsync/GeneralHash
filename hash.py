import hashlib,sys,random

try:
    HashMe = str(sys.argv[1])
except:
    print("Syntax : python {} 'Your String'".format(sys.argv[0]))
    sys.exit()


def HashString (StringToHash : str):
    Hash = hashlib.sha256(StringToHash.encode())
    return Hash.hexdigest()

def __save__ (Hash:str, RawString:str, FileNameStart = "Hashed", FileNameEnd = random.randint(10000,999999)) -> str:
    with open(f"{FileNameStart}{FileNameEnd}.txt", "a+") as SaveHash:  SaveHash.write("{h}:{s}\n".format(h=Hash, s=RawString))
    return "{}{}.txt".format(FileNameStart, FileNameEnd)


if __name__ == '__main__':
    print("SHA256 : ",HashString(HashMe))
    print("Identity : ",id(HashMe))
    print("PyHash : ",hash(HashMe))
    print("Len : ",len(sys.argv))
    print("> Saved hash:rawstr to [{}]".format(__save__(HashString(HashMe), HashMe)))