"""Phase-2 deep content for ga/static-gk. Run: py -3 static-gk.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from sg_part1 import build_books, build_sports, build_awards
from sg_part2 import build_days, build_symbols, build_orgs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Book ↔ author", "very common",
      "'Who wrote X', 'X is the autobiography of', 'the Booker-winning novel X was written by', match-the-column of books and authors.",
      "Split your revision into four racks: ancient/medieval texts (Kautilya, Kalhana, Kalidasa, Abul Fazl), freedom-era works (Gandhi, Nehru, Tagore, Bankim), autobiographies (Wings of Fire, Long Walk to Freedom, Playing It My Way) and Booker winners (Rushdie 1981, Roy 1997, Kiran Desai 2006, Adiga 2008). In match-the-column, strike options whose author belongs to another rack.",
      "books-authors",
      "Who is the author of **The Discovery of India**?",
      "**Jawaharlal Nehru**, written during imprisonment in 1942-46; his other work is Glimpses of World History."),
    P("Trophy / term ↔ sport, team size", "very common",
      "'Santosh/Thomas/Davis/Ryder trophy is associated with', 'googly/gambit/deuce belong to', 'how many players in a team of X'.",
      "Keep three lists: trophies by sport (cricket - Ranji and Ashes; football - Santosh and Durand; badminton - Thomas/Uber/Sudirman; tennis - Davis/Billie Jean King; golf - Ryder), terms by sport (bully-hockey, googly-cricket, birdie-golf, gambit-chess, deuce-tennis, bull's eye-shooting) and the odd team sizes (polo 4, basketball 5, volleyball 6, kabaddi/water polo 7, kho-kho 9, rugby 15).",
      "sports",
      "The **Thomas Cup** is associated with which sport?",
      "**Badminton** - the world men's team championship; the Uber Cup is its women's counterpart."),
    P("Award firsts & field", "common",
      "'First Bharat Ratna/Nobel/Param Vir Chakra', 'which award is given for coaching', 'Abel/Fields/Turing are given for', 'first recipient of X award'.",
      "Anchor each award to its first and its field: Bharat Ratna 1954 (trio Rajagopalachari-Radhakrishnan-Raman), Nobel ladder (Tagore 1913 first), PVC first Major Somnath Sharma, Jnanpith 1965 Kurup, Phalke 1969 Devika Rani, Khel Ratna first Anand. Fields: Abel-Fields = mathematics, Turing = computing, Dronacharya = coaches, Arjuna = players.",
      "awards",
      "The **Dronacharya Award** honours —",
      "Outstanding **coaches** who produce medal-winners; the Arjuna Award goes to sportspersons themselves."),
    P("Important day ↔ date / person", "common",
      "'Which day falls on 5 September', 'World Environment Day date', 'National Sports Day honours', calendar-matching questions.",
      "Two mini-tables settle everything. Person-linked dates: 12 Jan Vivekananda, 1 Jul B.C. Roy, 29 Aug Dhyan Chand, 5 Sep Radhakrishnan, 15 Sep Visvesvaraya, 14 Nov Nehru, 22 Dec Ramanujan. International dates: 22 Mar Water, 7 Apr Health (WHO 1948), 22 Apr Earth, 5 Jun Environment, 21 Jun Yoga, 16 Oct Food (FAO), 24 Oct UN, 10 Dec Human Rights (UDHR).",
      "important-days",
      "**World Environment Day** is observed on —",
      "**5 June** - the date the Stockholm Conference began in 1972; Earth Day is 22 April."),
    P("HQ / currency / parliament / national symbol", "occasional",
      "'Where is NATO/ADB/INTERPOL headquartered', 'currency of X', 'Knesset/Diet is the parliament of', 'national aquatic animal/heritage animal'.",
      "Group by city for HQs (New York - UN/UNICEF; Geneva - WHO/WTO/ILO; Paris - UNESCO; Rome - FAO; Nairobi - UNEP; Vienna - IAEA/OPEC; The Hague - ICJ; Brussels - NATO; Kathmandu - SAARC; Manila - ADB; Dubai - ICC; Lausanne - IOC; Lyon - INTERPOL) and by country for currencies (taka, ngultrum, kyat, baht, rand, real) and parliaments (Knesset-Israel, Diet-Japan, Majlis-Iran, Bundestag-Germany, Duma-Russia, Folketing-Denmark, Storting-Norway).",
      "organisations-countries",
      "The headquarters of the **International Cricket Council (ICC)** are in —",
      "**Dubai** (UAE); the ICC moved from Lord's, London, in 2005."),
    P("Olympics and world tournaments", "common",
      "'First modern Olympics', 'Olympic motto/rings', 'first FIFA/Cricket World Cup', 'India's first individual gold', marathon distance.",
      "One Olympics card: 1896 Athens (Coubertin, IOC 1894), motto Citius-Altius-Fortius, five rings = five continents, marathon 42.195 km; India - Pritchard 1900, hockey gold 1928, Jadhav 1952 first individual medal, Bindra 2008 first individual gold, Neeraj Chopra 2020. Tournaments: first FIFA World Cup 1930 (Uruguay), first Cricket World Cup 1975 (England; West Indies won), Ranji Trophy 1934.",
      "sports",
      "In which year was the **first Cricket World Cup** played?",
      "**1975** - hosted by England and won by the West Indies (India's first title came in 1983)."),
    P("Firsts in India", "common",
      "'First woman Governor/Chief Minister/President/IPS', 'first Field Marshal', 'first Indian in space', 'first railway/satellite/feature film', firsts matching.",
      "Keep the women-first list and the pioneering list separate. Women: Sarojini Naidu (Governor 1947), Sucheta Kripalani (CM 1963), Pratibha Patil (President 2007), Meira Kumar (Speaker 2009), Kiran Bedi (IPS 1972), Kalpana Chawla (space 1997), Bachendri Pal (Everest 1984). Pioneers: Rajendra Prasad, Nehru, Manekshaw (Field Marshal 1973), Rakesh Sharma (space 1984), Aryabhata (1975), Raja Harishchandra (1913), Bombay-Thane railway (1853), Chandrayaan-3 (23 August - National Space Day).",
      "national-symbols-firsts",
      "Who was India's **first woman IPS officer**?",
      "**Kiran Bedi** (joined the service in 1972)."),
]

if __name__ == "__main__":
    subs = [build_books(), build_sports(), build_awards(),
            build_days(), build_symbols(), build_orgs()]
    apply_topic("static-gk", subs, PYQ)
