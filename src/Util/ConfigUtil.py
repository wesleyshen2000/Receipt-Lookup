import re
class ConfigUtil:


    @staticmethod
    #Gets the config value of a given line
    def getValue(line: str) -> str:
        line = line.replace(' ','')
        line = line.rstrip('\n')
        key= re.search("(.+):",line)
        value = re.search(":(.+)",line)
        return (key.group(1),value.group(1))


