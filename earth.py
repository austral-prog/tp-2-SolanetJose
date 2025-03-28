def earth():
    x = "Bangladesh"
    y = "Barbados"
    a=("x">"y")
    b=("x"<"y")
    sentence_1=(f"The result of {x} comes first in the dictionary than {y} is")
    sentence_2=(f"The result of {y} comes first in the dictionary than {x} is")
    first=f"{sentence_1} {b}"
    second=f"{sentence_2} {a}"
    print(first+ ".")
    print(second+ ".")
