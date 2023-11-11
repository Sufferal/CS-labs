def clear_file(filename):
  with open(filename, "w") as f:
    f.write("a")

def add_spaces(filename, n):
  with open(filename, "r") as f:
    content = f.read()

  modified_content = ' ' * n + content

  with open(filename, "w") as f:
    f.write(modified_content)

def remove_lines(filename, n):
  with open(filename, "r") as f:
    content = f.readlines()

  modified_content = content[n:]

  with open(filename, "w") as f:
    f.writelines(modified_content)

def get_current_message():
  with open("message.txt", "r") as f:
    return f.read()

def set_original_msg():
  with open("message.txt", "w") as f:
    f.write("""modern western cryptology emerged directly from the flowering of modern diplomacy. the 
ambassadors' reports were sometimes opened and read, and, if necessary, crypt-analyzed. by the end of the 
century, cryptology had become important enough for most states to keep full-time cipher secretaries occupied 
in making up new keys, enciphering and deciphering messages, and solving intercepted dispatches. 
sometimes the cryptanalysts were separate from the cipher secretaries and were called in only when needed. 
perhaps the most elaborate organization was venice's. it fell under the immediate control of the council of ten, 
the powerful and mysterious body that ruled the republic largely through its efficient secret police. venice owed 
her preeminence largely to giovanni soro, who was perhaps the west's first great cryptanalyst. soro, appointed 
cipher secretary in 1506, enjoyed remarkable success in solving the ciphers of numerous principalities. his 
solution of a dispatch of mark anthony coloana, chief of the army of the holy roman emperor maximilian i, 
requesting 20,000 ducats or the presence of the emperor with the army, gave an insight into colonna's 
problems. so great wassoro's fame that other courts sharpened their ciphers, and as early as 1510 the papal 
curia was sending him ciphers that no one in rome could solve. but venice had no monopoly. in 1589, henry of 
navarre, who was destined to become the mostpopular king in the history of france (he coined the slogan "a 
chicken inevery peasant's pot every sunday"), ascended to the throne as henry ivand found himself embroiled 
still more fiercely in his bitter contestwith the holy league, a catholic faction that refused to concede that 
aprotestant could wear the crown. the league, headed by the duke of mayenne, held paris and all the other 
large cities of france, and was receiving large transfusions of men and money from philip of spain. henry was 
tightly hemmed in, and it was at this juncture that some correspondence between philip and two of his liaison 
officers,commander juan de moreo and ambassador manosse, fell into henry'shands.it was in cipher, but he 
had in his government at the time onefrancois viete, the seigneur de la bigotiere, a 49-year-old lawyer 
from poitou who had risen to become counselor of the parlement, or court ofjustice, of tours and a privy 
counselor to henry. viete had for yearsamused himself with mathematics as a hobby"never was a man 
moreborn for mathematics," said tallement des reaux. as the man who firstused letters for quantities in 
algebra, giving that study its characteristiclook, viete is today remembered as the father of algebra. a year 
before,he had solved a spanish dispatch addressed to alessandro farnese, theduke of parma, who headed the 
spanish forces of the league. henryturned the new intercepts over to him to see if viete could repeat hissuccess.""")