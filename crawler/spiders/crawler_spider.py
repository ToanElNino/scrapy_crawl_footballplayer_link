from time import sleep
from scrapy import Spider, Request
from scrapy.selector import Selector
from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["fbref.com"]

    def start_requests(self):
        dataAI = ["aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar", "as", "at", "au", "av", "aw", "ax", "ay", "az", 
                "ba", "bb", "be", "bg", "bh", "bi", "bj", "bk", "bl", "bn", "bo", "br", "bs", "bt", "bu", "bv", "bw", "by", "bz", 
                "ca", "cc", "cd", "ce", "ch", "ci", "cl", "cm", "co", "cr", "cs", "cu", "cv", "cw", "cy", "cz", 
                "da", "db", "dc", "de", "dg", "dh", "di", "dj", "dk", "dl", "dm", "do", "dr", "ds", "du", "dv", "dw", "dy", "dz", 
                "ea", "eb", "ec", "ed", "ee", "ef", "eg", "eh", "ei", "ej", "ek", "el", "em", "en", "eo", "ep", "eq", "er", "es", "et", "eu", "ev", "ew", "ex", "ey", "ez", 
                "fa", "fd", "fe", "fi", "fj", "fl", "fo", "fr", "ft", "fu", "fy", 
                "ga", "gb", "gc", "gd", "ge", "gf", "gh", "gi", "gj", "gk", "gl", "gm", "gn", "go", "gr", "gs", "gt", "gu", "gv", "gw", "gy",
                "ha", "hd", "he", "hi", "hj", "hl", "hm", "hn", "ho", "hr", "hs", "ht", "hu", "hv", "hw", "hy",
                "ia", "ib", "ic", "id", "ie", "if", "ig", "ih", "ii", "ij", "ik", "il", "im", "in", "io", "ip", "iq", "ir", "is", "it", "iu", "iv", "iw", "ix", "iy", "iz"
        ]
        dataJR = [
                "ja", "jb", "jd", "je", "jg", "jh", "ji", "jl", "jn", "jo", "jr", "ju", "jw", "jy",
                "ka", "kb", "kc", "kd", "ke", "kg", "kh", "ki", "kj", "kl", "km", "kn", "ko", "kp", "kr", "ks", "ku", "kv", "kw", "ky",
                "la", "le", "lg", "lh", "li", "lj", "lk", "ll", "lm", "lo", "lt", "lu", "lw", "ly",
                "ma", "mb", "mc", "md", "me", "mf", "mg", "mh", "mi", "mj", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz",
                "na", "nc", "nd", "ne", "nf", "ng", "nh", "ni", "nj", "nk", "nl", "nm", "nn", "no", "nr", "ns", "nt", "nu", "nw", "nx", "ny", "nz",
                "oa", "ob", "oc", "od", "oe", "of", "og", "oh", "oi", "oj", "ok", "ol", "om", "on", "oo", "op", "oq", "or", "os", "ot", "ou", "ov", "ow", "ox", "oy", "oz",
                "pa", "pc", "pe", "pf", "ph", "pi", "pj", "pl", "pm", "pn", "po", "pp", "pr", "ps", "pt", "pu", "pw", "py",
                "qa", "qe", "qi", "qo", "qr", "qt", "qu", "qv", "qw",
                "ra", "re", "rg", "rh", "ri", "rj", "rm", "rn", "ro", "rr", "ru", "rw", "ry", "rz",
        ]
        dataSZ = [
                "sa", "sb", "sc", "sd", "se", "sf", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sp", "sq", "sr", "ss", "st", "su", "sv", "sw", "sy", "sz"
                "ta", "tb", "tc", "te", "tf", "th", "ti", "tj", "tk", "tl", "tm", "to", "tp", "tr", "ts", "tt", "tu", "tv", "tw", "tx", "ty", "tz",
                "ua", "ub", "uc", "ud", "ue", "uf", "ug", "uh", "ui", "uj", "uk", "ul", "um", "un", "uo", "up", "uq", "ur", "us", "ut", "uu", "uv", "uw", "ux", "uy", "uz",
                "va", "ve", "vi", "vj", "vl", "vo", "vr", "vs", "vu", "vy",
                "wa", "wb", "wd", "we", "wh", "wi", "wl", "wn", "wo", "wr", "ws", "wu", "wy",
                "xa", "xe", "xh", "xi", "xo", "xu", "xv", "xy",
                "ya", "yb", "yc", "yd", "ye", "yf", "yg", "yh", "yi", "yk", "yl", "yn", "yo", "yp", "yr", "ys", "yt", "yu", "yv",
                "za", "zb", "zd", "ze", "zg", "zh", "zi", "zj", "zl", "zm", "zn", "zo", "zp", "zr", "zs", "zu", "zv", "zw", "zy"
        ]

        for i in dataSZ:
            url = f"https://fbref.com/en/players/{i}/" #https://fbref.com/en/players/aa
            yield Request(url=url, callback=self.parse)
            sleep(3)

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="section_content"]//p')
        for x in range(len(questions)-1):
            path = f'//div[@class="section_content"]//p[{x+1}]//a//@href'
            item = CrawlerItem()
            item['Link'] = Selector(response).xpath(path).extract_first()
            yield item