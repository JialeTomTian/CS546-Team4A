def Translation():
    # Description of the problem can be found at http://codeforces.com/problemset/problem/41/A

    s, t = input(), input()

    # This case isn't mentioned by the problem, but I don't want to be wrong.
    if len(s) != len(t):
        print("NO")
        quit()

    for index in range(len(s)):
        if s[index] != t[len(s) - index - 1]:
            print("NO")
            quit()

    print("YES")


def check(function):
    import io
    from unittest.mock import patch

    test_cases = [
        {"input": "code\nedoc", "output": "YES"},
        {"input": "abb\naba", "output": "NO"},
        {"input": "code\ncode", "output": "NO"},
        {"input": "abacaba\nabacaba", "output": "YES"},
        {"input": "q\nq", "output": "YES"},
        {"input": "asrgdfngfnmfgnhweratgjkk\nasrgdfngfnmfgnhweratgjkk", "output": "NO"},
        {"input": "z\na", "output": "NO"},
        {"input": "asd\ndsa", "output": "YES"},
        {"input": "abcdef\nfecdba", "output": "NO"},
        {
            "input": "ywjjbirapvskozubvxoemscfwl\ngnduubaogtfaiowjizlvjcu",
            "output": "NO",
        },
        {
            "input": "mfrmqxtzvgaeuleubcmcxcfqyruwzenguhgrmkuhdgnhgtgkdszwqyd\nmfxufheiperjnhyczclkmzyhcxntdfskzkzdwzzujdinf",
            "output": "NO",
        },
        {
            "input": "bnbnemvybqizywlnghlykniaxxxlkhftppbdeqpesrtgkcpoeqowjwhrylpsziiwcldodcoonpimudvrxejjo\ntiynnekmlalogyvrgptbinkoqdwzuiyjlrldxhzjmmp",
            "output": "NO",
        },
        {
            "input": "pwlpubwyhzqvcitemnhvvwkmwcaawjvdiwtoxyhbhbxerlypelevasmelpfqwjk\nstruuzebbcenziscuoecywugxncdwzyfozhljjyizpqcgkyonyetarcpwkqhuugsqjuixsxptmbnlfupdcfigacdhhrzb",
            "output": "NO",
        },
        {
            "input": "gdvqjoyxnkypfvdxssgrihnwxkeojmnpdeobpecytkbdwujqfjtxsqspxvxpqioyfagzjxupqqzpgnpnpxcuipweunqch\nkkqkiwwasbhezqcfeceyngcyuogrkhqecwsyerdniqiocjehrpkljiljophqhyaiefjpavoom",
            "output": "NO",
        },
        {"input": "umeszdawsvgkjhlqwzents\nhxqhdungbylhnikwviuh", "output": "NO"},
        {
            "input": "juotpscvyfmgntshcealgbsrwwksgrwnrrbyaqqsxdlzhkbugdyx\nibqvffmfktyipgiopznsqtrtxiijntdbgyy",
            "output": "NO",
        },
        {
            "input": "zbwueheveouatecaglziqmudxemhrsozmaujrwlqmppzoumxhamwugedikvkblvmxwuofmpafdprbcftew\nulczwrqhctbtbxrhhodwbcxwimncnexosksujlisgclllxokrsbnozthajnnlilyffmsyko",
            "output": "NO",
        },
        {
            "input": "nkgwuugukzcv\nqktnpxedwxpxkrxdvgmfgoxkdfpbzvwsduyiybynbkouonhvmzakeiruhfmvrktghadbfkmwxduoqv",
            "output": "NO",
        },
        {
            "input": "incenvizhqpcenhjhehvjvgbsnfixbatrrjstxjzhlmdmxijztphxbrldlqwdfimweepkggzcxsrwelodpnryntepioqpvk\ndhjbjjftlvnxibkklxquwmzhjfvnmwpapdrslioxisbyhhfymyiaqhlgecpxamqnocizwxniubrmpyubvpenoukhcobkdojlybxd",
            "output": "NO",
        },
        {"input": "w\nw", "output": "YES"},
        {"input": "vz\nzv", "output": "YES"},
        {"input": "ry\nyr", "output": "YES"},
        {"input": "xou\nuox", "output": "YES"},
        {"input": "axg\ngax", "output": "NO"},
        {"input": "zdsl\nlsdz", "output": "YES"},
        {"input": "kudl\nldku", "output": "NO"},
        {"input": "zzlzwnqlcl\nlclqnwzlzz", "output": "YES"},
        {"input": "vzzgicnzqooejpjzads\nsdazjpjeooqzncigzzv", "output": "YES"},
        {"input": "raqhmvmzuwaykjpyxsykr\nxkysrypjkyawuzmvmhqar", "output": "NO"},
        {
            "input": "ngedczubzdcqbxksnxuavdjaqtmdwncjnoaicvmodcqvhfezew\nwezefhvqcdomvciaonjcnwdmtqajdvauxnskxbqcdzbuzcdegn",
            "output": "YES",
        },
        {
            "input": "muooqttvrrljcxbroizkymuidvfmhhsjtumksdkcbwwpfqdyvxtrlymofendqvznzlmim\nmimlznzvqdnefomylrtxvydqfpwwbckdskmutjshhmfvdiumykziorbxcjlrrvttqooum",
            "output": "YES",
        },
        {
            "input": "vxpqullmcbegsdskddortcvxyqlbvxmmkhevovnezubvpvnrcajpxraeaxizgaowtfkzywvhnbgzsxbhkaipcmoumtikkiyyaivg\ngviayyikkitmuomcpiakhbxszgbnhvwyzkftwoagzixaearxpjacrnvpvbuzenvovehkmmxvblqyxvctroddksdsgebcmlluqpxv",
            "output": "YES",
        },
        {
            "input": "mnhaxtaopjzrkqlbroiyipitndczpunwygstmzevgyjdzyanxkdqnvgkikfabwouwkkbzuiuvgvxgpizsvqsbwepktpdrgdkmfdc\ncdfmkdgrdptkpewbsqvszipgxvgvuiuzbkkwuowbafkikgvnqdkxnayzdjygvezmtsgywnupocdntipiyiorblqkrzjpzatxahnm",
            "output": "NO",
        },
        {
            "input": "dgxmzbqofstzcdgthbaewbwocowvhqpinehpjatnnbrijcolvsatbblsrxabzrpszoiecpwhfjmwuhqrapvtcgvikuxtzbftydkw\nwkdytfbztxukivgctvparqhuwmjfhwpceiozsprzbaxrslbbqasvlocjirbnntajphenipthvwocowbweabhtgdcztsfoqbzmxgd",
            "output": "NO",
        },
        {
            "input": "gxoixiecetohtgjgbqzvlaobkhstejxdklghowtvwunnnvauriohuspsdmpzckprwajyxldoyckgjivjpmbfqtszmtocovxwgeh\nhegwxvocotmzstqfbmpjvijgkcyodlxyjawrpkczpmdspsuhoiruavnnnuwvtwohglkdxjetshkboalvzqbgjgthoteceixioxg",
            "output": "YES",
        },
        {
            "input": "sihxuwvmaambplxvjfoskinghzicyfqebjtkysotattkahssumfcgrkheotdxwjckpvapbkaepqrxseyfrwtyaycmrzsrsngkh\nhkgnsrszrmcyaytwrfyesxrqpeakbpavpkcjwxdtoehkrgcfmusshakttatosyktjbeqfycizhgniksofjvxlpbmaamvwuxhis",
            "output": "YES",
        },
        {
            "input": "ycnahksbughnonldzrhkysujmylcgcfuludjvjiahtkyzqvkopzqcnwhltbzfugzojqkjjlggmvnultascmygelkiktmfieok\nkoeifmtkiklegkmcsatlunvmggkjjlqjozgufzbtlhwncqzpokvqzykthaijvjdulufcgclymjusyyhrzdlnonhgubskhancy",
            "output": "NO",
        },
        {
            "input": "wbqasaehtkfojruzyhrlgwmtyiovmzyfifslvlemhqheyaelzwnthrenjsbmntwaoryzwfbxmscmypvxlfmzpnkkjlvwvmtz\nztmvwvljkknpzmflxvpymcsmxbfwzyroawtnmbsjnerhtnwzleayehqhmelvlsfifyzmvoiytmwglrhyzurjofktheasaqbw",
            "output": "YES",
        },
        {
            "input": "imippqurprbhfugngtgifelytadegwrgaefnfhbjjnmzikvjaccotqzemufqieqldgnbmviisgkynzeldlhqxuqphjfmyij\njiymfjhpquxqhldleznykgsiivmbngdlqeiqfumezqtoccajvkizmnjjbhfnfeagrwgedatylefigtgngufhbrpruqppimi",
            "output": "YES",
        },
        {
            "input": "bikydffiuisckpvzqlteqfhegsagimodb\nbdomigasgehfqetlqzvpkcsiuiffdykib",
            "output": "YES",
        },
    ]
    for i, case in enumerate(test_cases):
        input_val = case["input"]
        output = case["output"]
        with patch("builtins.input", side_effect=input_val.split("\n")):
            function()


if __name__ == "__main__":
    check(Translation)
    print("PASSED")
