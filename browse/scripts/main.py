from genOut import GenFiles
from topicsParser import TopicsParser
from filterdb import FilterType

f = GenFiles() # GenFiles object

# code to generate output markdown files

# all words
f.gen_out("../../database/db.csv", "../all.md", FilterType.ALL_WORDS)

# all missing words
f.gen_out("../../database/db.csv", "../currently_missing_words.md", FilterType.MISSING_WORDS, "Currently Missing Words")

# alphabets
f.gen_out("../../database/db.csv", "../alpha/a.md", FilterType.ALPHABET, "a")
f.gen_out("../../database/db.csv", "../alpha/b.md", FilterType.ALPHABET, "b")
f.gen_out("../../database/db.csv", "../alpha/c.md", FilterType.ALPHABET, "c")
f.gen_out("../../database/db.csv", "../alpha/d.md", FilterType.ALPHABET, "d")
f.gen_out("../../database/db.csv", "../alpha/e.md", FilterType.ALPHABET, "e")
f.gen_out("../../database/db.csv", "../alpha/f.md", FilterType.ALPHABET, "f")
f.gen_out("../../database/db.csv", "../alpha/g.md", FilterType.ALPHABET, "g")
f.gen_out("../../database/db.csv", "../alpha/h.md", FilterType.ALPHABET, "h")
f.gen_out("../../database/db.csv", "../alpha/i.md", FilterType.ALPHABET, "i")
f.gen_out("../../database/db.csv", "../alpha/j.md", FilterType.ALPHABET, "j")
f.gen_out("../../database/db.csv", "../alpha/k.md", FilterType.ALPHABET, "k")
f.gen_out("../../database/db.csv", "../alpha/l.md", FilterType.ALPHABET, "l")
f.gen_out("../../database/db.csv", "../alpha/m.md", FilterType.ALPHABET, "m")
f.gen_out("../../database/db.csv", "../alpha/n.md", FilterType.ALPHABET, "n")
f.gen_out("../../database/db.csv", "../alpha/o.md", FilterType.ALPHABET, "o")
f.gen_out("../../database/db.csv", "../alpha/p.md", FilterType.ALPHABET, "p")
f.gen_out("../../database/db.csv", "../alpha/q.md", FilterType.ALPHABET, "q")
f.gen_out("../../database/db.csv", "../alpha/r.md", FilterType.ALPHABET, "r")
f.gen_out("../../database/db.csv", "../alpha/s.md", FilterType.ALPHABET, "s")
f.gen_out("../../database/db.csv", "../alpha/t.md", FilterType.ALPHABET, "t")
f.gen_out("../../database/db.csv", "../alpha/u.md", FilterType.ALPHABET, "u")
f.gen_out("../../database/db.csv", "../alpha/v.md", FilterType.ALPHABET, "v")
f.gen_out("../../database/db.csv", "../alpha/w.md", FilterType.ALPHABET, "w")
f.gen_out("../../database/db.csv", "../alpha/x.md", FilterType.ALPHABET, "x")
f.gen_out("../../database/db.csv", "../alpha/y.md", FilterType.ALPHABET, "y")
f.gen_out("../../database/db.csv", "../alpha/z.md", FilterType.ALPHABET, "z")

# topics
tp = TopicsParser()
topics = tp.gen_topics("../../database/db.csv")
topics_file = open("../topics/00-topics-list.md", "w", encoding="UTF-8")
# topics list file - add heading
topics_file.write("Click on the topic to see words under it. \n \n")
for topic in topics:
    # generate individual topic files as per the topics-list
    f.gen_out("../../database/db.csv", '../topics/{}.md'.format(topic), FilterType.TOPIC, "{}".format(topic))
    # add a bulleted list of topics linking to the topic files
    topics_file.write("- [" + topic + "]" + "(" + "{}.md".format(topic) + ")" + "\n")
