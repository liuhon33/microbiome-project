from biom import parse_table
with open('american_gut.biom', encoding="utf8", errors='ignore') as f:
    table = parse_table(f)
    
#  encoding="utf8", errors='ignore'