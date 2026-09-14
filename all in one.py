import pickle, os

OUT = r"G:\Class 12 Projects\Computer project class 12\anime_full.dat"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

anime = [

# ---------------- Hindi (Dubbed) — Comedy (10) ----------------
["Shinchan", 1992, "Hindi", "Comedy", "TV Asahi", "Keiichi Hara", 8.4, "Anime", "30+", "22 min/ep", ["Akiko Yajima"], "A naughty child causes funny chaos in everyday life."],
["Doraemon", 1979, "Hindi", "Comedy", "TV Asahi", "Fujiko F. Fujio", 8.0, "Anime", "20+", "22 min/ep", ["Wasabi Mizuta"], "A robot cat helps a lazy boy with futuristic gadgets."],
["Crayon Shin-chan", 1992, "Hindi", "Comedy", "Shin-Ei Animation", "Keiichi Hara", 8.4, "Anime", "20+", "22 min/ep", ["Akiko Yajima"], "A hilarious preschooler’s mischievous adventures."],
["Kochikame", 1996, "Hindi", "Comedy", "Studio Gallop", "Atsutoshi Umezawa", 7.6, "Anime", "10", "25 min/ep", ["LaSalle Ishii"], "A police officer’s funny misadventures in Tokyo."],
["The Disastrous Life of Saiki K.", 2016, "Hindi", "Comedy", "J.C.Staff", "Hiroaki Sakurai", 8.3, "Anime", "3", "23 min/ep", ["Hiroshi Kamiya"], "A psychic teen hides his powers to live a normal life."],
["Gintama", 2006, "Hindi", "Comedy", "Sunrise", "Shinji Takamatsu", 9.0, "Anime", "8", "24 min/ep", ["Tomokazu Sugita"], "Samurai and aliens collide in a hilarious sci-fi parody."],
["One Punch Man", 2015, "Hindi", "Comedy", "Madhouse", "Shingo Natsume", 8.7, "Anime", "2", "24 min/ep", ["Makoto Furukawa"], "A superhero bored of winning every fight with one punch."],
["Komi Can’t Communicate", 2021, "Hindi", "Comedy", "OLM", "Ayumu Watanabe", 8.1, "Anime", "2", "23 min/ep", ["Aoi Koga"], "A shy girl seeks 100 friends with help from her classmate."],
["Spy × Family", 2022, "Hindi", "Comedy", "Wit Studio/CloverWorks", "Kazuhiro Furuhashi", 8.6, "Anime", "2", "25 min/ep", ["Takuya Eguchi"], "A spy, assassin, and telepath form a fake family."],
["Kaguya-sama: Love Is War", 2019, "Hindi", "Comedy", "A-1 Pictures", "Mamoru Hatakeyama", 8.5, "Anime", "3", "24 min/ep", ["Aoi Koga"], "Two geniuses battle to make the other confess love first."],

# ---------------- Hindi (Dubbed) — Action (10) ----------------
["Naruto", 2002, "Hindi", "Action", "Studio Pierrot", "Hayato Date", 8.4, "Anime", "9", "23 min/ep", ["Junko Takeuchi"], "A young ninja dreams of becoming the Hokage."],
["Naruto: Shippuden", 2007, "Hindi", "Action", "Studio Pierrot", "Hayato Date", 8.7, "Anime", "21", "23 min/ep", ["Junko Takeuchi"], "Naruto faces stronger enemies and matures as a hero."],
["Attack on Titan", 2013, "Hindi", "Action", "MAPPA/Wit Studio", "Tetsurō Araki", 9.1, "Anime", "4", "25 min/ep", ["Yuki Kaji"], "Humans battle gigantic Titans for survival."],
["Dragon Ball Z", 1989, "Hindi", "Action", "Toei Animation", "Daisuke Nishio", 8.8, "Anime", "9", "24 min/ep", ["Masako Nozawa"], "Goku defends Earth through epic battles."],
["My Hero Academia", 2016, "Hindi", "Action", "Bones", "Kenji Nagasaki", 8.3, "Anime", "6", "24 min/ep", ["Daiki Yamashita"], "Students train to become professional heroes."],
["Bleach", 2004, "Hindi", "Action", "Studio Pierrot", "Noriyuki Abe", 8.2, "Anime", "16", "24 min/ep", ["Masakazu Morita"], "A teen gains powers to fight evil spirits."],
["One Piece", 1999, "Hindi", "Action", "Toei Animation", "Konosuke Uda", 8.9, "Anime", "20+", "24 min/ep", ["Mayumi Tanaka"], "Pirate Luffy sails to find the legendary treasure."],
["Demon Slayer: Kimetsu no Yaiba", 2019, "Hindi", "Action", "Ufotable", "Haruo Sotozaki", 8.7, "Anime", "3", "24 min/ep", ["Natsuki Hanae"], "A boy fights demons to save his sister."],
["Fullmetal Alchemist: Brotherhood", 2009, "Hindi", "Action", "Bones", "Yasuhiro Irie", 9.1, "Anime", "1", "24 min/ep", ["Romi Park"], "Two brothers seek redemption through alchemy."],
["Tokyo Revengers", 2021, "Hindi", "Action", "Liden Films", "Koichi Hatsumi", 8.0, "Anime", "3", "25 min/ep", ["Yuuki Shin"], "A man travels back in time to save his friends from gangs."],

# ---------------- Hindi (Dubbed) — Sci-Fi (10) ----------------
["Steins;Gate", 2011, "Hindi", "Sci-Fi", "White Fox", "Hiroshi Hamasaki", 9.1, "Anime", "1", "24 min/ep", ["Mamoru Miyano"], "A scientist discovers time travel with dire consequences."],
["Psycho-Pass", 2012, "Hindi", "Sci-Fi", "Production I.G", "Naoyoshi Shiotani", 8.2, "Anime", "3", "23 min/ep", ["Kana Hanazawa"], "In a future where crime is predicted by tech, justice is redefined."],
["Ergo Proxy", 2006, "Hindi", "Sci-Fi", "Manglobe", "Shuko Murase", 8.0, "Anime", "1", "25 min/ep", ["Rie Saitō"], "Humans and androids coexist in a dystopian city."],
["Parasyte: The Maxim", 2014, "Hindi", "Sci-Fi", "Madhouse", "Kenichi Shimizu", 8.3, "Anime", "1", "24 min/ep", ["Nobunaga Shimazaki"], "A boy’s hand is possessed by an alien parasite."],
["Cowboy Bebop", 1998, "Hindi", "Sci-Fi", "Sunrise", "Shinichirō Watanabe", 8.9, "Anime", "1", "24 min/ep", ["Koichi Yamadera"], "Bounty hunters travel through space chasing criminals."],
["Neon Genesis Evangelion", 1995, "Hindi", "Sci-Fi", "Gainax", "Hideaki Anno", 8.5, "Anime", "1", "25 min/ep", ["Megumi Ogata"], "Teen pilots control giant mechas to fight monsters."],
["Dr. Stone", 2019, "Hindi", "Sci-Fi", "TMS Entertainment", "Shinya Iino", 8.1, "Anime", "3", "25 min/ep", ["Yusuke Kobayashi"], "A genius rebuilds civilization using science after petrification."],
["Erased", 2016, "Hindi", "Sci-Fi", "A-1 Pictures", "Tomohiko Itō", 8.5, "Anime", "1", "24 min/ep", ["Tao Tsuchiya"], "A man travels to the past to prevent a tragedy."],
["Chainsaw Man", 2022, "Hindi", "Sci-Fi", "MAPPA", "Ryu Nakayama", 8.7, "Anime", "1", "24 min/ep", ["Kikunosuke Toya"], "A devil hunter merges with his pet demon to survive."],
["86 -Eighty Six-", 2021, "Hindi", "Sci-Fi", "A-1 Pictures", "Toshimasa Ishii", 8.3, "Anime", "2", "24 min/ep", ["Shōya Chiba"], "War, politics, and AI collide in this mecha story."],

# ---------------- Hindi (Dubbed) — Crime-Thriller (10) ----------------
["Death Note", 2006, "Hindi", "Crime-Thriller", "Madhouse", "Tetsurō Araki", 9.0, "Anime", "1", "23 min/ep", ["Mamoru Miyano"], "A student finds a notebook that kills anyone whose name is written in it."],
["Monster", 2004, "Hindi", "Crime-Thriller", "Madhouse", "Masayuki Kojima", 8.8, "Anime", "1", "24 min/ep", ["Kentarō Itō"], "A doctor hunts a psychopathic killer he once saved."],
["Terror in Resonance", 2014, "Hindi", "Crime-Thriller", "MAPPA", "Shinichirō Watanabe", 8.0, "Anime", "1", "23 min/ep", ["Kaito Ishikawa"], "Two teens plan terror acts to reveal truth about the government."],
["Erased", 2016, "Hindi", "Crime-Thriller", "A-1 Pictures", "Tomohiko Itō", 8.5, "Anime", "1", "24 min/ep", ["Tao Tsuchiya"], "A man travels to his childhood to stop a serial killer."],
["Paranoia Agent", 2004, "Hindi", "Crime-Thriller", "Madhouse", "Satoshi Kon", 8.0, "Anime", "1", "24 min/ep", ["Shozo Iizuka"], "A mysterious boy attacks Tokyo residents with a bat."],
["Black Lagoon", 2006, "Hindi", "Crime-Thriller", "Madhouse", "Sunao Katabuchi", 8.0, "Anime", "2", "24 min/ep", ["Megumi Toyoguchi"], "Mercenaries operate in a lawless Southeast Asian city."],
["Psycho-Pass", 2012, "Hindi", "Crime-Thriller", "Production I.G", "Naoyoshi Shiotani", 8.2, "Anime", "3", "23 min/ep", ["Kana Hanazawa"], "Detectives fight crime using futuristic judgment systems."],
["Joker Game", 2016, "Hindi", "Crime-Thriller", "Production I.G", "Kazuya Nomura", 7.7, "Anime", "1", "24 min/ep", ["Yoshimasa Hosoya"], "Spies use cunning and deception during WWII."],
["91 Days", 2016, "Hindi", "Crime-Thriller", "Shuka", "Hiro Kaburagi", 8.1, "Anime", "1", "24 min/ep", ["Takashi Kondo"], "A man seeks revenge on the mafia that killed his family."],
["Baccano!", 2007, "Hindi", "Crime-Thriller", "Brain’s Base", "Takashi Hashimoto", 8.4, "Anime", "1", "23 min/ep", ["Masaya Onosaka"], "Interconnected stories of immortality and crime in 1930s America."],

# ---------------- Hindi (Dubbed) — Drama (10) ----------------
["Your Lie in April", 2014, "Hindi", "Drama", "A-1 Pictures", "Kyohei Ishiguro", 8.6, "Anime", "1", "22 min/ep", ["Natsuki Hanae"], "A pianist finds inspiration after meeting a free-spirited violinist."],
["Clannad: After Story", 2008, "Hindi", "Drama", "Kyoto Animation", "Tatsuya Ishihara", 8.9, "Anime", "1", "25 min/ep", ["Mai Nakahara"], "A touching story about family, loss, and love."],
["Vivy: Fluorite Eye’s Song", 2021, "Hindi", "Drama", "Wit Studio", "Shinpei Ezaki", 8.3, "Anime", "1", "24 min/ep", ["Atsumi Tanezaki"], "An AI singer tries to prevent humanity’s extinction."],
["A Silent Voice", 2016, "Hindi", "Drama", "Kyoto Animation", "Naoko Yamada", 8.4, "Anime", "1", "2h10m", ["Saori Hayami"], "A boy seeks forgiveness from a deaf girl he once bullied."],
["Toradora!", 2008, "Hindi", "Drama", "J.C.Staff", "Tatsuyuki Nagai", 8.0, "Anime", "1", "24 min/ep", ["Rie Kugimiya"], "Two teens help each other win their crushes and find love."],
["March Comes in Like a Lion", 2016, "Hindi", "Drama", "Shaft", "Akiyuki Shinbo", 8.7, "Anime", "2", "24 min/ep", ["Kengo Kawanishi"], "A young shogi player battles depression and isolation."],
["Anohana: The Flower We Saw That Day", 2011, "Hindi", "Drama", "A-1 Pictures", "Tatsuyuki Nagai", 8.2, "Anime", "1", "23 min/ep", ["Ai Kayano"], "Childhood friends reunite to help a ghost find peace."],
["Barakamon", 2014, "Hindi", "Drama", "Kinema Citrus", "Masaki Tachibana", 8.2, "Anime", "1", "23 min/ep", ["Daisuke Ono"], "A calligrapher finds new meaning in life after exile."],
["Fruits Basket", 2019, "Hindi", "Drama", "TMS Entertainment", "Yoshihide Ibata", 8.6, "Anime", "3", "24 min/ep", ["Manaka Iwami"], "A kind girl discovers a family cursed to transform into zodiac animals."],
["Made in Abyss", 2017, "Hindi", "Drama", "Kinema Citrus", "Masayuki Kojima", 8.4, "Anime", "2", "25 min/ep", ["Miyu Tomita"], "A girl descends into a mysterious abyss to find her mother."],

# ---------------- Hindi (Dubbed) — Educational (10) ----------------
["Cells at Work!", 2018, "Hindi", "Educational", "David Production", "Kenichi Suzuki", 8.1, "Anime", "2", "24 min/ep", ["Kana Hanazawa"], "Anthropomorphized cells explain how the human body works."],
["Dr. Stone", 2019, "Hindi", "Educational", "TMS Entertainment", "Shinya Iino", 8.1, "Anime", "3", "25 min/ep", ["Yusuke Kobayashi"], "A scientific journey rebuilding civilization from scratch."],
["Silver Spoon", 2013, "Hindi", "Educational", "A-1 Pictures", "Tomohiko Itō", 8.1, "Anime", "2", "23 min/ep", ["Ryohei Kimura"], "A student learns life lessons at an agricultural school."],
["Shirobako", 2014, "Hindi", "Educational", "P.A.Works", "Tsutomu Mizushima", 8.3, "Anime", "2", "23 min/ep", ["Juri Kimura"], "Behind the scenes of anime production and teamwork."],
["Moyashimon", 2007, "Hindi", "Educational", "Telecom Animation Film", "Yūichirō Yano", 7.6, "Anime", "2", "23 min/ep", ["Tomokazu Seki"], "A student who can see microbes learns fermentation science."],
["Bokura wa Minna Kawaisou", 2014, "Hindi", "Educational", "Brain’s Base", "Shigeyuki Miya", 7.7, "Anime", "1", "24 min/ep", ["Kana Hanazawa"], "Learning life and growth through humor."],
["Great Teacher Onizuka", 1999, "Hindi", "Educational", "Studio Pierrot", "Noriyuki Abe", 8.5, "Anime", "1", "24 min/ep", ["Toshiyuki Morikawa"], "A biker-turned-teacher inspires and reforms students."],
["Ascendance of a Bookworm", 2019, "Hindi", "Educational", "Ajia-do", "Mitsuru Hongo", 8.0, "Anime", "3", "23 min/ep", ["Yuka Iguchi"], "A book-loving girl brings literacy to a medieval world."],
["Bakuman", 2010, "Hindi", "Educational", "J.C.Staff", "Kenichi Kasai", 8.3, "Anime", "3", "24 min/ep", ["Atsushi Abe"], "Two teens pursue their dream of becoming manga creators."],
["Mushishi", 2005, "Hindi", "Educational", "Artland", "Hiroshi Nagahama", 8.7, "Anime", "2", "25 min/ep", ["Yuto Nakano"], "A mysterious man studies lifeforms invisible to most humans."],
]

# ---------------- English — Comedy (10) ----------------
anime += [
["The Disastrous Life of Saiki K.", 2016, "English", "Comedy", "J.C.Staff", "Hiroaki Sakurai", 8.3, "Anime", "3", "23 min/ep", ["Hiroshi Kamiya"], "A psychic teen hides his powers to live a normal life."],
["Nichijou: My Ordinary Life", 2011, "English", "Comedy", "Kyoto Animation", "Tatsuya Ishihara", 8.4, "Anime", "1", "24 min/ep", ["Misuzu Togashi"], "Absurd comedy showing everyday randomness of students."],
["KonoSuba: God’s Blessing on This Wonderful World!", 2016, "English", "Comedy", "Studio Deen", "Takaomi Kanasaki", 8.1, "Anime", "2", "23 min/ep", ["Jun Fukushima"], "A gamer dies and is reborn in a hilarious fantasy world."],
["Grand Blue", 2018, "English", "Comedy", "Zero-G", "Shinji Takamatsu", 8.0, "Anime", "1", "24 min/ep", ["Yuma Uchida"], "College life, diving, and wild comedy antics."],
["Daily Lives of High School Boys", 2012, "English", "Comedy", "Sunrise", "Shinji Takamatsu", 8.0, "Anime", "1", "24 min/ep", ["Kenichi Suzumura"], "Three friends endure hilarious school misadventures."],
["Asobi Asobase", 2018, "English", "Comedy", "Lerche", "Seiji Kishi", 8.2, "Anime", "1", "24 min/ep", ["Hina Kino"], "Three girls’ absurd school games lead to endless laughs."],
["Ouran High School Host Club", 2006, "English", "Comedy", "Bones", "Takuya Igarashi", 8.2, "Anime", "1", "23 min/ep", ["Maaya Sakamoto"], "A girl joins a host club pretending to be a boy."],
["Prison School", 2015, "English", "Comedy", "J.C.Staff", "Tsutomu Mizushima", 7.6, "Anime", "1", "24 min/ep", ["Hiroshi Kamiya"], "Boys in a strict girls’ school face comic punishment."],
["Detroit Metal City", 2008, "English", "Comedy", "Studio 4°C", "Hiroshi Nagahama", 8.1, "Anime", "1", "13 min/ep", ["Yoshihiko Hosoda"], "A mild man leads a double life as a death-metal star."],
["Aggretsuko", 2018, "English", "Comedy", "Fanworks", "Rarecho", 8.0, "Anime", "5", "15 min/ep", ["Kaolip"], "A red panda vents office stress through death-metal karaoke."],
]

# ---------------- English — Action (10) ----------------
anime += [
["Attack on Titan", 2013, "English", "Action", "MAPPA/Wit Studio", "Tetsurō Araki", 9.1, "Anime", "4", "25 min/ep", ["Yuki Kaji"], "Humans battle gigantic Titans for survival."],
["One Punch Man", 2015, "English", "Action", "Madhouse", "Shingo Natsume", 8.7, "Anime", "2", "24 min/ep", ["Makoto Furukawa"], "A superhero bored of winning every fight with one punch."],
["Demon Slayer: Kimetsu no Yaiba", 2019, "English", "Action", "Ufotable", "Haruo Sotozaki", 8.7, "Anime", "3", "24 min/ep", ["Natsuki Hanae"], "A boy fights demons to save his sister."],
["Vinland Saga", 2019, "English", "Action", "Wit Studio", "Shuhei Yabuta", 8.8, "Anime", "2", "24 min/ep", ["Yuto Uemura"], "A Viking warrior seeks revenge in medieval Europe."],
["Fullmetal Alchemist: Brotherhood", 2009, "English", "Action", "Bones", "Yasuhiro Irie", 9.1, "Anime", "1", "24 min/ep", ["Romi Park"], "Two brothers seek redemption through alchemy."],
["Samurai Champloo", 2004, "English", "Action", "Manglobe", "Shinichirō Watanabe", 8.5, "Anime", "1", "24 min/ep", ["Kazuya Nakai"], "Samurai adventure mixing hip-hop and Edo-era Japan."],
["Bleach: Thousand-Year Blood War", 2022, "English", "Action", "Studio Pierrot", "Tomohisa Taguchi", 9.0, "Anime", "2", "24 min/ep", ["Masakazu Morita"], "The final epic war between Soul Reapers and Quincy."],
["Rurouni Kenshin", 1996, "English", "Action", "Studio Gallop", "Kazuhiro Furuhashi", 8.5, "Anime", "3", "25 min/ep", ["Mayo Suzukaze"], "A swordsman vows never to kill again while defending peace."],
["Sword Art Online", 2012, "English", "Action", "A-1 Pictures", "Tomohiko Itō", 7.9, "Anime", "4", "24 min/ep", ["Yoshitsugu Matsuoka"], "Players trapped in a virtual world must survive to escape."],
["Jujutsu Kaisen", 2020, "English", "Action", "MAPPA", "Sunghoo Park", 8.6, "Anime", "2", "24 min/ep", ["Junya Enoki"], "A student fights curses using mystical powers."],
]

# ---------------- English — Sci-Fi (10) ----------------
anime += [
["Steins;Gate", 2011, "English", "Sci-Fi", "White Fox", "Hiroshi Hamasaki", 9.1, "Anime", "1", "24 min/ep", ["Mamoru Miyano"], "A scientist discovers time travel with dire consequences."],
["Cowboy Bebop", 1998, "English", "Sci-Fi", "Sunrise", "Shinichirō Watanabe", 8.9, "Anime", "1", "24 min/ep", ["Koichi Yamadera"], "Bounty hunters travel through space chasing criminals."],
["Neon Genesis Evangelion", 1995, "English", "Sci-Fi", "Gainax", "Hideaki Anno", 8.5, "Anime", "1", "25 min/ep", ["Megumi Ogata"], "Teen pilots control giant mechas to fight monsters."],
["Ghost in the Shell: Stand Alone Complex", 2002, "English", "Sci-Fi", "Production I.G", "Kenji Kamiyama", 8.5, "Anime", "2", "25 min/ep", ["Atsuko Tanaka"], "Cyborg agents fight crime in a futuristic Japan."],
["Planetes", 2003, "English", "Sci-Fi", "Sunrise", "Goro Taniguchi", 8.2, "Anime", "1", "25 min/ep", ["Kazunari Tanaka"], "Space debris collectors deal with moral and social dilemmas."],
["Ergo Proxy", 2006, "English", "Sci-Fi", "Manglobe", "Shuko Murase", 8.0, "Anime", "1", "25 min/ep", ["Rie Saitō"], "Humans and androids coexist in a dystopian city."],
["Serial Experiments Lain", 1998, "English", "Sci-Fi", "Triangle Staff", "Ryutaro Nakamura", 8.1, "Anime", "1", "23 min/ep", ["Kaori Shimizu"], "A girl explores the boundary between reality and cyberspace."],
["Psycho-Pass", 2012, "English", "Sci-Fi", "Production I.G", "Naoyoshi Shiotani", 8.2, "Anime", "3", "23 min/ep", ["Kana Hanazawa"], "In a future where crime is predicted by tech, justice is redefined."],
["Dr. Stone", 2019, "English", "Sci-Fi", "TMS Entertainment", "Shinya Iino", 8.1, "Anime", "3", "25 min/ep", ["Yusuke Kobayashi"], "A genius rebuilds civilization using science after petrification."],
["Parasyte: The Maxim", 2014, "English", "Sci-Fi", "Madhouse", "Kenichi Shimizu", 8.3, "Anime", "1", "24 min/ep", ["Nobunaga Shimazaki"], "A boy’s hand is possessed by an alien parasite."],
]

# ---------------- English — Crime-Thriller (10) ----------------
anime += [
["Death Note", 2006, "English", "Crime-Thriller", "Madhouse", "Tetsurō Araki", 9.0, "Anime", "1", "23 min/ep", ["Mamoru Miyano"], "A student finds a notebook that kills anyone whose name is written in it."],
["Monster", 2004, "English", "Crime-Thriller", "Madhouse", "Masayuki Kojima", 8.8, "Anime", "1", "24 min/ep", ["Kentarō Itō"], "A doctor hunts a psychopathic killer he once saved."],
["Terror in Resonance", 2014, "English", "Crime-Thriller", "MAPPA", "Shinichirō Watanabe", 8.0, "Anime", "1", "23 min/ep", ["Kaito Ishikawa"], "Two teens plan terror acts to reveal truth about the government."],
["Erased", 2016, "English", "Crime-Thriller", "A-1 Pictures", "Tomohiko Itō", 8.5, "Anime", "1", "24 min/ep", ["Tao Tsuchiya"], "A man travels to his childhood to stop a serial killer."],
["Baccano!", 2007, "English", "Crime-Thriller", "Brain’s Base", "Takashi Hashimoto", 8.4, "Anime", "1", "23 min/ep", ["Masaya Onosaka"], "Interconnected stories of immortality and crime in 1930s America."],
["Black Lagoon", 2006, "English", "Crime-Thriller", "Madhouse", "Sunao Katabuchi", 8.0, "Anime", "2", "24 min/ep", ["Megumi Toyoguchi"], "Mercenaries operate in a lawless Southeast Asian city."],
["Joker Game", 2016, "English", "Crime-Thriller", "Production I.G", "Kazuya Nomura", 7.7, "Anime", "1", "24 min/ep", ["Yoshimasa Hosoya"], "Spies use cunning and deception during WWII."],
["91 Days", 2016, "English", "Crime-Thriller", "Shuka", "Hiro Kaburagi", 8.1, "Anime", "1", "24 min/ep", ["Takashi Kondo"], "A man seeks revenge on the mafia that killed his family."],
["Higurashi: When They Cry", 2006, "English", "Crime-Thriller", "Studio Deen", "Chiaki Kon", 8.0, "Anime", "2", "24 min/ep", ["Soichiro Hoshi"], "Dark secrets unfold in a seemingly peaceful village."],
["Paranoia Agent", 2004, "English", "Crime-Thriller", "Madhouse", "Satoshi Kon", 8.0, "Anime", "1", "24 min/ep", ["Shozo Iizuka"], "A mysterious boy attacks Tokyo residents with a bat."],
]

# ---------------- English — Drama (10) ----------------
anime += [
["Your Lie in April", 2014, "English", "Drama", "A-1 Pictures", "Kyohei Ishiguro", 8.6, "Anime", "1", "22 min/ep", ["Natsuki Hanae"], "A pianist finds inspiration after meeting a free-spirited violinist."],
["Clannad: After Story", 2008, "English", "Drama", "Kyoto Animation", "Tatsuya Ishihara", 8.9, "Anime", "1", "25 min/ep", ["Mai Nakahara"], "A touching story about family, loss, and love."],
["Anohana: The Flower We Saw That Day", 2011, "English", "Drama", "A-1 Pictures", "Tatsuyuki Nagai", 8.2, "Anime", "1", "23 min/ep", ["Ai Kayano"], "Childhood friends reunite to help a ghost find peace."],
["Fruits Basket", 2019, "English", "Drama", "TMS Entertainment", "Yoshihide Ibata", 8.6, "Anime", "3", "24 min/ep", ["Manaka Iwami"], "A girl discovers a family cursed to transform into zodiac animals."],
["A Silent Voice", 2016, "English", "Drama", "Kyoto Animation", "Naoko Yamada", 8.4, "Anime", "1", "2h10m", ["Saori Hayami"], "A boy seeks forgiveness from a deaf girl he once bullied."],
["March Comes in Like a Lion", 2016, "English", "Drama", "Shaft", "Akiyuki Shinbo", 8.7, "Anime", "2", "24 min/ep", ["Kengo Kawanishi"], "A young shogi player battles depression and isolation."],
["Toradora!", 2008, "English", "Drama", "J.C.Staff", "Tatsuyuki Nagai", 8.0, "Anime", "1", "24 min/ep", ["Rie Kugimiya"], "Two teens help each other win their crushes and find love."],
["Barakamon", 2014, "English", "Drama", "Kinema Citrus", "Masaki Tachibana", 8.2, "Anime", "1", "23 min/ep", ["Daisuke Ono"], "A calligrapher finds new meaning in life after exile."],
["Made in Abyss", 2017, "English", "Drama", "Kinema Citrus", "Masayuki Kojima", 8.4, "Anime", "2", "25 min/ep", ["Miyu Tomita"], "A girl descends into a mysterious abyss to find her mother."],
["Vivy: Fluorite Eye’s Song", 2021, "English", "Drama", "Wit Studio", "Shinpei Ezaki", 8.3, "Anime", "1", "24 min/ep", ["Atsumi Tanezaki"], "An AI singer tries to prevent humanity’s extinction."],
]

# ---------------- English — Educational (10) ----------------
anime += [
["Cells at Work!", 2018, "English", "Educational", "David Production", "Kenichi Suzuki", 8.1, "Anime", "2", "24 min/ep", ["Kana Hanazawa"], "Anthropomorphized cells explain how the human body works."],
["Dr. Stone", 2019, "English", "Educational", "TMS Entertainment", "Shinya Iino", 8.1, "Anime", "3", "25 min/ep", ["Yusuke Kobayashi"], "A scientific journey rebuilding civilization from scratch."],
["Silver Spoon", 2013, "English", "Educational", "A-1 Pictures", "Tomohiko Itō", 8.1, "Anime", "2", "23 min/ep", ["Ryohei Kimura"], "A student learns life lessons at an agricultural school."],
["Shirobako", 2014, "English", "Educational", "P.A.Works", "Tsutomu Mizushima", 8.3, "Anime", "2", "23 min/ep", ["Juri Kimura"], "Behind the scenes of anime production and teamwork."],
["Moyashimon", 2007, "English", "Educational", "Telecom Animation Film", "Yūichirō Yano", 7.6, "Anime", "2", "23 min/ep", ["Tomokazu Seki"], "A student who can see microbes learns fermentation science."],
["Great Teacher Onizuka", 1999, "English", "Educational", "Studio Pierrot", "Noriyuki Abe", 8.5, "Anime", "1", "24 min/ep", ["Toshiyuki Morikawa"], "A biker-turned-teacher inspires and reforms students."],
["Bakuman", 2010, "English", "Educational", "J.C.Staff", "Kenichi Kasai", 8.3, "Anime", "3", "24 min/ep", ["Atsushi Abe"], "Two teens pursue their dream of becoming manga creators."],
["Mushishi", 2005, "English", "Educational", "Artland", "Hiroshi Nagahama", 8.7, "Anime", "2", "25 min/ep", ["Yuto Nakano"], "A mysterious man studies lifeforms invisible to most humans."],
["Bartender", 2006, "English", "Educational", "Palm Studio", "Masaki Watanabe", 7.9, "Anime", "1", "23 min/ep", ["Keiji Fujiwara"], "A bartender uses cocktails to heal customers’ hearts."],
["Kaiji: Ultimate Survivor", 2007, "English", "Educational", "Madhouse", "Yuzo Sato", 8.2, "Anime", "2", "24 min/ep", ["Masato Hagiwara"], "A man learns about risk, trust, and survival through gambling."],
]


# ---------------- Bengali — Comedy (10) ----------------
anime += [
["Doraemon", 1979, "Bengali", "Comedy", "Shin-Ei Animation", "Fujiko F. Fujio", 8.0, "Anime", "20+", "22 min/ep", ["Nobita","Doraemon"], "A robotic cat helps a lazy boy with futuristic gadgets."],
["Shinchan", 1992, "Bengali", "Comedy", "Shin-Ei Animation", "Keiichi Hara", 8.4, "Anime", "20+", "22 min/ep", ["Shinchan Nohara"], "A mischievous preschooler creates hilarious situations."],
["Chhota Bheem", 2008, "Bengali", "Comedy", "Green Gold Animation", "Rajiv Chilaka", 6.9, "Cartoon", "15", "22 min/ep", ["Bheem","Chutki"], "A brave boy of Dholakpur saves his village with friends."],
["Tom and Jerry", 1940, "Bengali", "Comedy", "Warner Bros.", "William Hanna", 9.0, "Cartoon", "6+", "7 min/ep", ["Tom","Jerry"], "Classic cat and mouse chases filled with slapstick comedy."],
["Oggy and the Cockroaches", 1998, "Bengali", "Comedy", "Gaumont", "Olivier Jean-Marie", 7.3, "Cartoon", "6+", "7 min/ep", ["Oggy","Joey"], "A blue cat is constantly troubled by cockroaches."],
["Motu Patlu", 2013, "Bengali", "Comedy", "Cosmos Maya", "Suhas Kadav", 7.2, "Cartoon", "14", "23 min/ep", ["Motu","Patlu"], "Two friends get into hilarious trouble in Furfuri Nagar."],
["Roll No. 21", 2010, "Bengali", "Comedy", "Cosmos Maya", "Ankur Chauhan", 7.8, "Cartoon", "5", "23 min/ep", ["Kris","Principal"], "Modern-day Krishna battles demon friends in school life."],
["Mr. Bean: The Animated Series", 2002, "Bengali", "Comedy", "Tiger Aspect", "Richard Purdum", 7.0, "Cartoon", "5", "22 min/ep", ["Mr. Bean"], "An eccentric man faces funny everyday problems."],
["Pakdam Pakdai (Rat-A-Tat)", 2013, "Bengali", "Comedy", "Nickelodeon India", "Miriam Mayer", 6.9, "Cartoon", "3", "22 min/ep", ["Doggy Don","Chhotu"], "Dogs and mice engage in endless funny chases."],
["Titoo", 2022, "Bengali", "Comedy", "Cosmos Maya", "Anish Patel", 7.1, "Cartoon", "2", "22 min/ep", ["Titoo"], "A naughty boy’s daily mischiefs bring laughter to everyone."],
]

# ---------------- Bengali — Action (10) ----------------
anime += [
["Dragon Ball Z", 1989, "Bengali", "Action", "Toei Animation", "Daisuke Nishio", 8.8, "Anime", "9", "24 min/ep", ["Goku","Vegeta"], "Warriors fight epic battles to protect the universe."],
["Pokémon", 1997, "Bengali", "Action", "OLM", "Kunihiko Yuyama", 7.5, "Anime", "25+", "24 min/ep", ["Ash","Pikachu"], "A boy dreams of becoming a Pokémon master."],
["Beyblade", 2001, "Bengali", "Action", "Madhouse", "Takao Aoki", 6.9, "Anime", "4", "22 min/ep", ["Tyson","Kai"], "Teens battle with mystical spinning tops."],
["Power Rangers SPD", 2005, "Bengali", "Action", "Disney", "Koichi Sakamoto", 6.6, "Cartoon", "1", "22 min/ep", ["Bridge Carson"], "Future cops protect Earth from alien threats."],
["Teen Titans Go!", 2013, "Bengali", "Action", "Warner Bros.", "Aaron Horvath", 6.7, "Cartoon", "8", "22 min/ep", ["Robin","Starfire"], "Teen superheroes save the world with humor."],
["Ben 10", 2005, "Bengali", "Action", "Cartoon Network", "Man of Action", 7.5, "Cartoon", "4", "22 min/ep", ["Ben Tennyson"], "A boy with an alien watch transforms to fight evil."],
["Ultimate Spider-Man", 2012, "Bengali", "Action", "Marvel", "Alex Soto", 7.2, "Cartoon", "4", "22 min/ep", ["Peter Parker"], "Spider-Man trains with S.H.I.E.L.D. to become the best hero."],
["Justice League Unlimited", 2004, "Bengali", "Action", "Warner Bros.", "James Tucker", 8.9, "Cartoon", "3", "23 min/ep", ["Batman","Superman"], "DC’s heroes unite to save the world from villains."],
["Ninja Hattori", 1981, "Bengali", "Action", "Shin-Ei Animation", "Fujiko Fujio", 7.2, "Anime", "3", "22 min/ep", ["Hattori","Kenichi"], "A ninja helps a boy handle school and bullies."],
["Chakra The Invincible", 2013, "Bengali", "Action", "Graphic India", "Sharad Devarajan", 6.8, "Cartoon", "1", "24 min/ep", ["Chakra"], "An Indian superhero fights to defend Mumbai from villains."],
]

# ---------------- Bengali — Sci-Fi (10) ----------------
anime += [
["Astro Boy", 2003, "Bengali", "Sci-Fi", "Tezuka Productions", "Kazuya Konaka", 7.1, "Anime", "1", "24 min/ep", ["Astro"], "A robot boy fights for peace and equality."],
["Transformers Prime", 2010, "Bengali", "Sci-Fi", "Hasbro", "Robert Orci", 8.0, "Cartoon", "3", "23 min/ep", ["Optimus Prime"], "Autobots battle Decepticons to save Earth."],
["Iron Man: Armored Adventures", 2008, "Bengali", "Sci-Fi", "Marvel Animation", "Yoshikazu Iwanami", 6.6, "Cartoon", "2", "22 min/ep", ["Tony Stark"], "Teen Tony builds advanced armor to fight evil."],
["Generator Rex", 2010, "Bengali", "Sci-Fi", "Cartoon Network", "Man of Action", 7.7, "Cartoon", "3", "23 min/ep", ["Rex"], "A teen with nanites uses powers to stop mutations."],
["Big Hero 6: The Series", 2017, "Bengali", "Sci-Fi", "Disney", "Mark McCorkle", 7.1, "Cartoon", "3", "22 min/ep", ["Hiro Hamada"], "Boy genius and robot Baymax fight tech villains."],
["Johnny Test", 2005, "Bengali", "Sci-Fi", "Warner Bros.", "Scott Fellows", 6.7, "Cartoon", "6", "22 min/ep", ["Johnny"], "A boy becomes his sisters’ experiment subject for science."],
["Buzz Lightyear of Star Command", 2000, "Bengali", "Sci-Fi", "Pixar", "Tad Stones", 6.9, "Cartoon", "2", "22 min/ep", ["Buzz Lightyear"], "Space ranger defends the galaxy from Emperor Zurg."],
["The Jetsons", 1962, "Bengali", "Sci-Fi", "Hanna-Barbera", "William Hanna", 7.0, "Cartoon", "3", "25 min/ep", ["George Jetson"], "A futuristic family navigates space-age life."],
["Jimmy Neutron: Boy Genius", 2002, "Bengali", "Sci-Fi", "Nickelodeon", "John A. Davis", 6.9, "Cartoon", "3", "23 min/ep", ["Jimmy Neutron"], "A genius boy invents gadgets that often go wrong."],
["Dexter’s Laboratory", 1996, "Bengali", "Sci-Fi", "Cartoon Network", "Genndy Tartakovsky", 8.0, "Cartoon", "4", "22 min/ep", ["Dexter"], "A genius boy hides a secret lab under his home."],
]

# ---------------- Bengali — Crime-Thriller (10) ----------------
anime += [
["Batman: The Animated Series", 1992, "Bengali", "Crime-Thriller", "Warner Bros.", "Bruce Timm", 9.0, "Cartoon", "4", "22 min/ep", ["Kevin Conroy"], "Batman fights crime and his rogues’ gallery in Gotham."],
["Detective Conan", 1996, "Bengali", "Crime-Thriller", "TMS Entertainment", "Kenji Kodama", 8.5, "Anime", "20+", "23 min/ep", ["Minami Takayama"], "A teenage detective trapped in a child’s body solves cases."],
["Scooby-Doo! Mystery Incorporated", 2010, "Bengali", "Crime-Thriller", "Warner Bros.", "Spike Brandt", 8.0, "Cartoon", "2", "22 min/ep", ["Scooby-Doo","Shaggy"], "Teens solve supernatural mysteries with comic twists."],
["Carmen Sandiego", 2019, "Bengali", "Crime-Thriller", "Netflix", "Jos Humphrey", 8.1, "Cartoon", "4", "24 min/ep", ["Gina Rodriguez"], "A modern Robin Hood thief steals from villains worldwide."],
["The Batman", 2004, "Bengali", "Crime-Thriller", "Warner Bros.", "Duane Capizzi", 7.8, "Cartoon", "5", "22 min/ep", ["Rino Romano"], "A young Batman faces new threats in Gotham City."],
["Totally Spies!", 2001, "Bengali", "Crime-Thriller", "Marathon Media", "Stéphane Berry", 7.0, "Cartoon", "6", "22 min/ep", ["Sam","Clover","Alex"], "Teen spies juggle school and secret missions."],
["Kim Possible", 2002, "Bengali", "Crime-Thriller", "Disney", "Mark McCorkle", 7.2, "Cartoon", "4", "22 min/ep", ["Kim Possible"], "A teenage girl saves the world between classes."],
["Inspector Gadget", 1983, "Bengali", "Crime-Thriller", "DIC Entertainment", "Andy Heyward", 7.3, "Cartoon", "2", "23 min/ep", ["Don Adams"], "A bionic detective fights crime with gadgets and luck."],
["The Amazing Spiez!", 2009, "Bengali", "Crime-Thriller", "Marathon Media", "Stéphane Berry", 6.5, "Cartoon", "2", "22 min/ep", ["Lee","Tony","Megan"], "Four siblings secretly work as international spies."],
["The Owl House", 2020, "Bengali", "Crime-Thriller", "Disney", "Dana Terrace", 8.4, "Cartoon", "3", "24 min/ep", ["Sarah-Nicole Robles"], "A girl enters a magical world full of secrets and rebellion."],
]

# ---------------- Bengali — Drama (10) ----------------
anime += [
["Avatar: The Last Airbender", 2005, "Bengali", "Drama", "Nickelodeon", "Bryan Konietzko", 9.3, "Cartoon", "3", "23 min/ep", ["Aang","Katara"], "A boy must master elements to bring peace to the world."],
["The Legend of Korra", 2012, "Bengali", "Drama", "Nickelodeon", "Michael Dante DiMartino", 8.3, "Cartoon", "4", "23 min/ep", ["Korra"], "The Avatar reincarnates and faces modern struggles."],
["How to Train Your Dragon: Riders of Berk", 2012, "Bengali", "Drama", "DreamWorks", "John Sanford", 8.0, "Cartoon", "8", "22 min/ep", ["Hiccup","Toothless"], "Vikings and dragons coexist in harmony and conflict."],
["Big City Greens", 2018, "Bengali", "Drama", "Disney", "Shane Houghton", 7.8, "Cartoon", "4", "22 min/ep", ["Cricket Green"], "A country boy experiences the chaos of city life."],
["Adventure Time", 2010, "Bengali", "Drama", "Cartoon Network", "Pendleton Ward", 8.6, "Cartoon", "10", "22 min/ep", ["Finn","Jake"], "A boy and dog explore a post-apocalyptic magical world."],
["Steven Universe", 2013, "Bengali", "Drama", "Cartoon Network", "Rebecca Sugar", 8.2, "Cartoon", "5", "23 min/ep", ["Zach Callison"], "A boy protects Earth with his family of magical Gems."],
["Dragon Prince", 2018, "Bengali", "Drama", "Netflix", "Aaron Ehasz", 8.3, "Cartoon", "5", "25 min/ep", ["Jack De Sena"], "Two princes and an elf work to end a magical war."],
["Miraculous: Tales of Ladybug & Cat Noir", 2015, "Bengali", "Drama", "Zagtoon", "Thomas Astruc", 7.6, "Cartoon", "5", "22 min/ep", ["Marinette","Adrien"], "Two teens secretly save Paris as superheroes."],
["She-Ra and the Princesses of Power", 2018, "Bengali", "Drama", "Netflix", "Noelle Stevenson", 8.1, "Cartoon", "5", "24 min/ep", ["Aimee Carrero"], "A soldier discovers her destiny as a legendary warrior."],
["Teen Titans", 2003, "Bengali", "Drama", "Warner Bros.", "Glen Murakami", 8.9, "Cartoon", "5", "23 min/ep", ["Robin","Raven"], "Teen superheroes navigate friendship and destiny."],
]

# ---------------- Bengali — Educational (10) ----------------
anime += [
["Sid the Science Kid", 2008, "Bengali", "Educational", "Jim Henson Company", "Brian Henson", 6.9, "Cartoon", "2", "23 min/ep", ["Sid"], "A curious boy explores science in daily life."],
["Octonauts", 2010, "Bengali", "Educational", "Silvergate Media", "Darragh O’Connell", 7.8, "Cartoon", "5", "23 min/ep", ["Captain Barnacles"], "Animals explore the ocean to rescue sea creatures."],
["Dinosaur Train", 2009, "Bengali", "Educational", "PBS", "Craig Bartlett", 7.0, "Cartoon", "4", "23 min/ep", ["Buddy"], "A dinosaur travels through time to learn science."],
["Wild Kratts", 2011, "Bengali", "Educational", "PBS Kids", "Martin Kratt", 7.8, "Cartoon", "6", "25 min/ep", ["Chris","Martin"], "Brothers teach wildlife biology through adventure."],
["Magic School Bus Rides Again", 2017, "Bengali", "Educational", "Netflix", "Richard Weston", 6.5, "Cartoon", "2", "23 min/ep", ["Ms. Frizzle"], "Kids learn science through magical field trips."],
["Handy Manny", 2006, "Bengali", "Educational", "Disney", "Roger Bollen", 6.7, "Cartoon", "3", "22 min/ep", ["Manny"], "A handyman teaches teamwork and problem-solving."],
["Art with Mati and Dada", 2013, "Bengali", "Educational", "Rai Fiction", "Massimo Carrier Ragazzi", 7.3, "Cartoon", "1", "10 min/ep", ["Mati","Dada"], "Kids learn art history through animated fun."],
["Peep and the Big Wide World", 2004, "Bengali", "Educational", "WGBH", "Sandra Schmirler", 7.5, "Cartoon", "3", "22 min/ep", ["Peep"], "Young chicks learn science through nature."]]




print("✅ English Anime dataset saved successfully (added to Hindi)!")

with open(OUT, "wb") as h:
    pickle.dump(anime, h)

print("✅ Anime dataset (Hindi + English) saved successfully!")


import pickle, os

OUT = r"G:\Class 12 Projects\Computer project class 12\webseries_full.dat"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

webseries = [

# ---------------- Hindi — Comedy (10) ----------------
["TVF Pitchers", 2015, "Hindi", "Comedy", "TVF", "Arunabh Kumar", 9.0, "Web Series", "2", "35 min/ep", ["Naveen Kasturia","Jitendra Kumar"], "Four friends quit their jobs to start a startup."],
["Panchayat", 2020, "Hindi", "Comedy", "Amazon Prime", "Deepak Kumar Mishra", 8.9, "Web Series", "3", "35 min/ep", ["Jitendra Kumar","Raghubir Yadav"], "A city engineer adjusts to life in a rural village office."],
["Gullak", 2019, "Hindi", "Comedy", "SonyLIV", "Amrit Raj Gupta", 9.0, "Web Series", "4", "30 min/ep", ["Jameel Khan","Geetanjali Kulkarni"], "Wholesome tales from a middle-class Indian family."],
["College Romance", 2018, "Hindi", "Comedy", "TVF", "Simarpreet Singh", 8.3, "Web Series", "4", "25 min/ep", ["Apoorva Arora","Keshav Sadhna"], "Friends explore love and life in college."],
["Hostel Daze", 2019, "Hindi", "Comedy", "Amazon Prime", "Raghav Subbu", 8.5, "Web Series", "4", "30 min/ep", ["Adarsh Gourav","Nikhil Vijay"], "Engineering hostel life full of chaos and bonding."],
["Permanent Roommates", 2014, "Hindi", "Comedy", "TVF", "Sameer Saxena", 8.7, "Web Series", "2", "30 min/ep", ["Sumeet Vyas","Nidhi Singh"], "A couple deals with modern love and commitment."],
["Humorously Yours", 2016, "Hindi", "Comedy", "TVF", "Vipul Goyal", 8.6, "Web Series", "2", "28 min/ep", ["Vipul Goyal","Rasika Dugal"], "A stand-up comedian juggles fame and life."],
["Little Things", 2016, "Hindi", "Comedy", "Netflix", "Dhruv Sehgal", 8.2, "Web Series", "4", "28 min/ep", ["Dhruv Sehgal","Mithila Palkar"], "A couple explores the beauty of everyday life."],
["What the Folks!", 2017, "Hindi", "Comedy", "Dice Media", "Ruchir Arun", 8.1, "Web Series", "3", "25 min/ep", ["Eisha Chopra","Veer Rajwant Singh"], "Modern family dynamics told with humor."],
["The Aam Aadmi Family", 2016, "Hindi", "Comedy", "The Timeliners", "Sumit Sobti", 8.0, "Web Series", "4", "22 min/ep", ["Brijendra Kala","Lubna Salim"], "Everyday hilarity of an average Indian family."],

# ---------------- Hindi — Action (10) ----------------
["The Family Man", 2019, "Hindi", "Action", "Amazon Prime", "Raj & DK", 8.7, "Web Series", "2", "45 min/ep", ["Manoj Bajpayee","Priyamani"], "A middle-class man secretly works as an intelligence officer."],
["Mirzapur", 2018, "Hindi", "Action", "Amazon Prime", "Karan Anshuman", 8.5, "Web Series", "3", "50 min/ep", ["Pankaj Tripathi","Ali Fazal"], "Crime, power and family feuds in a small town."],
["Special OPS", 2020, "Hindi", "Action", "Disney+ Hotstar", "Neeraj Pandey", 8.6, "Web Series", "1", "45 min/ep", ["Kay Kay Menon","Karan Tacker"], "RAW agent tracks a terrorist over years."],
["Bard of Blood", 2019, "Hindi", "Action", "Netflix", "Ribhu Dasgupta", 6.8, "Web Series", "1", "45 min/ep", ["Emraan Hashmi","Sobhita Dhulipala"], "An ex-spy is sent on a mission in Balochistan."],
["Asur: Welcome to Your Dark Side", 2020, "Hindi", "Action", "Voot", "Oni Sen", 8.4, "Web Series", "2", "45 min/ep", ["Arshad Warsi","Barun Sobti"], "A mythological crime thriller mixing science and faith."],
["Rana Naidu", 2023, "Hindi", "Action", "Netflix", "Karan Anshuman", 7.1, "Web Series", "1", "46 min/ep", ["Rana Daggubati","Venkatesh Daggubati"], "A problem solver in Bollywood's dark world."],
["The Forgotten Army", 2020, "Hindi", "Action", "Amazon Prime", "Kabir Khan", 7.3, "Web Series", "1", "45 min/ep", ["Sunny Kaushal","Sharvari Wagh"], "Story of Netaji’s Azad Hind Fauj."],
["Arya", 2020, "Hindi", "Action", "Disney+ Hotstar", "Ram Madhvani", 7.8, "Web Series", "3", "50 min/ep", ["Sushmita Sen"], "A mother turned crime boss fights to protect her family."],
["Inside Edge", 2017, "Hindi", "Action", "Amazon Prime", "Karan Anshuman", 7.9, "Web Series", "3", "45 min/ep", ["Vivek Oberoi","Richa Chadha"], "Cricket, politics and crime collide."],
["Criminal Justice", 2019, "Hindi", "Action", "Disney+ Hotstar", "Tigmanshu Dhulia", 8.1, "Web Series", "3", "48 min/ep", ["Pankaj Tripathi","Vikrant Massey"], "A gripping legal drama with intense action."],

# ---------------- Hindi — Sci-Fi (10) ----------------
["JL50", 2020, "Hindi", "Sci-Fi", "SonyLIV", "Shailender Vyas", 7.4, "Web Series", "1", "40 min/ep", ["Abhay Deol","Pankaj Kapur"], "A mysterious plane crash that defies time."],
["OK Computer", 2021, "Hindi", "Sci-Fi", "Disney+ Hotstar", "Neil Pagedar", 6.2, "Web Series", "1", "35 min/ep", ["Vijay Varma","Radhika Apte"], "A futuristic satire about AI and ethics."],
["Upload (Dubbed)", 2020, "Hindi", "Sci-Fi", "Amazon Prime", "Greg Daniels", 8.0, "Web Series", "3", "30 min/ep", ["Robbie Amell","Andy Allo"], "A man uploads his mind to a digital afterlife."],
["Leila", 2019, "Hindi", "Sci-Fi", "Netflix", "Deepa Mehta", 5.6, "Web Series", "1", "45 min/ep", ["Huma Qureshi"], "A dystopian future divided by class and purity."],
["The Last Hour", 2021, "Hindi", "Sci-Fi", "Amazon Prime", "Amit Kumar", 7.1, "Web Series", "1", "42 min/ep", ["Sanjay Kapoor","Karma Takapa"], "A shaman joins a cop to solve crimes using time visions."],
["Grahan", 2021, "Hindi", "Sci-Fi", "Disney+ Hotstar", "Ranjan Chandel", 8.5, "Web Series", "1", "45 min/ep", ["Pawan Malhotra","Wamiqa Gabbi"], "A police officer uncovers links between past and present."],
["Typewriter", 2019, "Hindi", "Sci-Fi", "Netflix", "Suhasini Sarkar", 6.5, "Web Series", "1", "40 min/ep", ["Palomi Ghosh"], "Children set out to capture a ghost in Goa."],
["Betaal", 2020, "Hindi", "Sci-Fi", "Netflix", "Patrick Graham", 5.4, "Web Series", "1", "40 min/ep", ["Vineet Kumar Singh"], "An undead colonial army resurfaces in India."],
["Tooth Pari: When Love Bites", 2023, "Hindi", "Sci-Fi", "Netflix", "Pratim D. Gupta", 6.5, "Web Series", "1", "45 min/ep", ["Shantanu Maheshwari","Tanya Maniktala"], "A fantasy love story between a vampire and human."],
["Crash Course", 2022, "Hindi", "Sci-Fi", "Amazon Prime", "Vijay Maurya", 7.2, "Web Series", "1", "45 min/ep", ["Annu Kapoor"], "A fictionalized look at coaching institutes; semi-scientific learning."],

# ---------------- Hindi — Crime-Thriller (10) ----------------
["Sacred Games", 2018, "Hindi", "Crime-Thriller", "Netflix", "Anurag Kashyap", 8.6, "Web Series", "2", "50 min/ep", ["Nawazuddin Siddiqui","Saif Ali Khan"], "A cop and a gangster’s story in the dark underbelly of Mumbai."],
["Delhi Crime", 2019, "Hindi", "Crime-Thriller", "Netflix", "Richie Mehta", 8.5, "Web Series", "2", "50 min/ep", ["Shefali Shah","Rasika Dugal"], "Based on the 2012 Delhi gang rape investigation."],
["Breathe", 2018, "Hindi", "Crime-Thriller", "Amazon Prime", "Mayank Sharma", 8.3, "Web Series", "3", "50 min/ep", ["R. Madhavan","Amit Sadh"], "A desperate father commits crimes to save his son."],
["Paatal Lok", 2020, "Hindi", "Crime-Thriller", "Amazon Prime", "Avinash Arun", 8.0, "Web Series", "1", "45 min/ep", ["Jaideep Ahlawat"], "A gritty crime thriller exploring class divides."],
["Rana Naidu", 2023, "Hindi", "Crime-Thriller", "Netflix", "Karan Anshuman", 7.1, "Web Series", "1", "46 min/ep", ["Rana Daggubati"], "A fixer for Bollywood faces family chaos."],
["Criminal Justice", 2019, "Hindi", "Crime-Thriller", "Hotstar", "Tigmanshu Dhulia", 8.1, "Web Series", "3", "48 min/ep", ["Pankaj Tripathi"], "A courtroom drama full of tension."],
["Asur: Welcome to Your Dark Side", 2020, "Hindi", "Crime-Thriller", "Voot", "Oni Sen", 8.4, "Web Series", "2", "45 min/ep", ["Arshad Warsi"], "A mythological thriller blending religion and crime."],
["Khakee: The Bihar Chapter", 2022, "Hindi", "Crime-Thriller", "Netflix", "Bhav Dhulia", 8.3, "Web Series", "1", "50 min/ep", ["Karan Tacker","Avinash Tiwary"], "A cop hunts a notorious criminal in Bihar."],
["Rangbaaz", 2018, "Hindi", "Crime-Thriller", "ZEE5", "Bhav Dhulia", 8.2, "Web Series", "3", "45 min/ep", ["Saqib Saleem"], "A gangster’s rise inspired by real events."],
["Aar Ya Paar", 2022, "Hindi", "Crime-Thriller", "Disney+ Hotstar", "Sidharth Sengupta", 7.0, "Web Series", "1", "44 min/ep", ["Aditya Rawal"], "A tribal man fights corruption and exploitation."],

# ---------------- Hindi — Drama (10) ----------------
["Made in Heaven", 2019, "Hindi", "Drama", "Amazon Prime", "Zoya Akhtar", 8.3, "Web Series", "2", "50 min/ep", ["Sobhita Dhulipala","Arjun Mathur"], "Two wedding planners navigate modern Indian society."],
["Mumbai Diaries 26/11", 2021, "Hindi", "Drama", "Amazon Prime", "Nikkhil Advani", 8.5, "Web Series", "2", "50 min/ep", ["Mohit Raina","Konkona Sen Sharma"], "Hospital staff face the Mumbai attacks."],
["Scam 1992: The Harshad Mehta Story", 2020, "Hindi", "Drama", "SonyLIV", "Hansal Mehta", 9.3, "Web Series", "1", "50 min/ep", ["Pratik Gandhi"], "The rise and fall of stockbroker Harshad Mehta."],
["Rocket Boys", 2022, "Hindi", "Drama", "SonyLIV", "Abhay Pannu", 9.2, "Web Series", "2", "45 min/ep", ["Jim Sarbh","Ishwak Singh"], "The story of India’s space pioneers."],
["Yeh Meri Family", 2018, "Hindi", "Drama", "TVF", "Sameer Saxena", 9.0, "Web Series", "2", "30 min/ep", ["Vishesh Bansal","Monica Chaudhary"], "A nostalgic drama set in the 1990s middle-class India."],
["Aspirants", 2021, "Hindi", "Drama", "TVF", "Apoorv Singh Karki", 9.1, "Web Series", "2", "35 min/ep", ["Naveen Kasturia","Shivankit Singh Parihar"], "UPSC aspirants face life's exams beyond the syllabus."],
["Kota Factory", 2019, "Hindi", "Drama", "TVF", "Raghav Subbu", 9.2, "Web Series", "2", "40 min/ep", ["Jitendra Kumar","Mayur More"], "Students prepare for IIT in the competitive city of Kota."],
["Tabbar", 2021, "Hindi", "Drama", "SonyLIV", "Ajitpal Singh", 8.3, "Web Series", "1", "45 min/ep", ["Pavan Malhotra","Supriya Pathak"], "A family caught in moral dilemmas after a crime."],
["Paatal Lok", 2020, "Hindi", "Drama", "Amazon Prime", "Avinash Arun", 8.0, "Web Series", "1", "45 min/ep", ["Jaideep Ahlawat"], "A hard-hitting social drama wrapped in thriller tones."],
["Suzhal: The Vortex", 2022, "Hindi", "Drama", "Amazon Prime", "Pushkar-Gayathri", 8.3, "Web Series", "1", "50 min/ep", ["Kathir","Aishwarya Rajesh"], "A crime and social drama in a small town."],

# ---------------- Hindi — Educational (10) ----------------
["Crash Course", 2022, "Hindi", "Educational", "Amazon Prime", "Vijay Maurya", 7.2, "Web Series", "1", "45 min/ep", ["Annu Kapoor"], "A drama about coaching institutes and student life."],
["Aspirants", 2021, "Hindi", "Educational", "TVF", "Apoorv Singh Karki", 9.1, "Web Series", "2", "35 min/ep", ["Naveen Kasturia"], "UPSC aspirants struggle and grow together."],
["Kota Factory", 2019, "Hindi", "Educational", "TVF", "Raghav Subbu", 9.2, "Web Series", "2", "40 min/ep", ["Jitendra Kumar"], "Black-and-white portrayal of students preparing for IIT."],
["Engineering Girls", 2018, "Hindi", "Educational", "The Timeliners", "Apoorv Singh Karki", 7.4, "Web Series", "2", "25 min/ep", ["Barkha Singh","Kritika Avasthi"], "Girls navigate friendship and studies in engineering college."],
["Laakhon Mein Ek", 2017, "Hindi", "Educational", "Amazon Prime", "Biswa Kalyan Rath", 8.2, "Web Series", "2", "30 min/ep", ["Ritwik Sahore"], "A satire on the pressure of coaching culture."],
["Operation MBBS", 2020, "Hindi", "Educational", "Dice Media", "Amrit Raj Gupta", 8.3, "Web Series", "2", "28 min/ep", ["Ayush Mehra"], "The journey of medical students navigating their first year."],
["Selection Day", 2018, "Hindi", "Educational", "Netflix", "Udayan Prasad", 7.3, "Web Series", "1", "30 min/ep", ["Mohammad Samad"], "Two brothers chase their cricket dreams with discipline."],
["Jeena Isi Ka Naam Hai", 2021, "Hindi", "Educational", "YouTube", "Arunabh Kumar", 7.0, "Web Series", "1", "25 min/ep", ["Various TVF Artists"], "Lessons from everyday life experiences."],
["School Days", 2022, "Hindi", "Educational", "Amazon MiniTV", "Various", 7.5, "Web Series", "1", "25 min/ep", ["Aditya Pandey"], "Light-hearted tales from a modern Indian school."],
["TVF Tripling", 2016, "Hindi", "Educational", "TVF", "Sameer Saxena", 8.5, "Web Series", "3", "28 min/ep", ["Sumeet Vyas"], "Siblings rediscover life and love through travel."],
]


# ---------------- English — Comedy (10) ----------------
webseries += [
["The Office (US)", 2005, "English", "Comedy", "NBC", "Greg Daniels", 9.0, "Web Series", "9", "22 min/ep", ["Steve Carell","John Krasinski"], "Mockumentary on office employees at Dunder Mifflin."],
["Brooklyn Nine-Nine", 2013, "English", "Comedy", "NBC", "Michael Schur", 8.4, "Web Series", "8", "22 min/ep", ["Andy Samberg","Andre Braugher"], "Detectives solve crimes with humor in Brooklyn’s 99th precinct."],
["Friends", 1994, "English", "Comedy", "NBC", "David Crane", 8.9, "Web Series", "10", "22 min/ep", ["Jennifer Aniston","Courteney Cox"], "Six friends navigate life and love in New York City."],
["The Big Bang Theory", 2007, "English", "Comedy", "CBS", "Chuck Lorre", 8.1, "Web Series", "12", "22 min/ep", ["Jim Parsons","Johnny Galecki"], "Geeky scientists find humor in science and relationships."],
["How I Met Your Mother", 2005, "English", "Comedy", "CBS", "Carter Bays", 8.3, "Web Series", "9", "22 min/ep", ["Josh Radnor","Neil Patrick Harris"], "A father narrates how he met their mother through funny tales."],
["Modern Family", 2009, "English", "Comedy", "ABC", "Christopher Lloyd", 8.4, "Web Series", "11", "22 min/ep", ["Sofía Vergara","Ty Burrell"], "A mockumentary about three diverse family types."],
["Parks and Recreation", 2009, "English", "Comedy", "NBC", "Greg Daniels", 8.6, "Web Series", "7", "22 min/ep", ["Amy Poehler","Nick Offerman"], "Optimistic bureaucrat works for her quirky small-town government."],
["The Marvelous Mrs. Maisel", 2017, "English", "Comedy", "Prime Video", "Amy Sherman-Palladino", 8.7, "Web Series", "5", "55 min/ep", ["Rachel Brosnahan"], "A 1950s housewife becomes a stand-up comedian."],
["Ted Lasso", 2020, "English", "Comedy", "Apple TV+", "Bill Lawrence", 8.8, "Web Series", "3", "45 min/ep", ["Jason Sudeikis"], "An American football coach manages a British soccer team."],
["The Good Place", 2016, "English", "Comedy", "NBC", "Michael Schur", 8.2, "Web Series", "4", "22 min/ep", ["Kristen Bell","Ted Danson"], "A woman ends up in the afterlife by mistake."],
]

# ---------------- English — Action (10) ----------------
webseries += [
["The Boys", 2019, "English", "Action", "Prime Video", "Eric Kripke", 8.7, "Web Series", "4", "50 min/ep", ["Karl Urban","Jack Quaid"], "Vigilantes take on corrupt superheroes."],
["Jack Ryan", 2018, "English", "Action", "Prime Video", "Carlton Cuse", 8.0, "Web Series", "4", "50 min/ep", ["John Krasinski"], "CIA analyst uncovers global conspiracies."],
["Reacher", 2022, "English", "Action", "Prime Video", "Nick Santora", 8.1, "Web Series", "2", "50 min/ep", ["Alan Ritchson"], "Drifter Jack Reacher solves crimes across America."],
["Daredevil", 2015, "English", "Action", "Netflix", "Drew Goddard", 8.6, "Web Series", "3", "50 min/ep", ["Charlie Cox"], "Blind lawyer fights crime as vigilante Daredevil."],
["The Punisher", 2017, "English", "Action", "Netflix", "Steve Lightfoot", 8.5, "Web Series", "2", "50 min/ep", ["Jon Bernthal"], "Marine seeks justice for his family’s murder."],
["Peacemaker", 2022, "English", "Action", "HBO Max", "James Gunn", 8.3, "Web Series", "1", "45 min/ep", ["John Cena"], "Anti-hero seeks redemption through chaos."],
["Money Heist", 2017, "English", "Action", "Netflix", "Álex Pina", 8.2, "Web Series", "5", "45 min/ep", ["Álvaro Morte"], "Criminals execute an ambitious Spanish heist."],
["Vikings", 2013, "English", "Action", "History Channel", "Michael Hirst", 8.5, "Web Series", "6", "45 min/ep", ["Travis Fimmel"], "Epic saga of Norse warriors."],
["The Mandalorian", 2019, "English", "Action", "Disney+", "Jon Favreau", 8.7, "Web Series", "3", "45 min/ep", ["Pedro Pascal"], "A bounty hunter in the Star Wars universe."],
["The Last of Us", 2023, "English", "Action", "HBO", "Craig Mazin", 9.1, "Web Series", "1", "60 min/ep", ["Pedro Pascal","Bella Ramsey"], "Survivors journey across post-apocalyptic America."],
]

# ---------------- English — Sci-Fi (10) ----------------
webseries += [
["Stranger Things", 2016, "English", "Sci-Fi", "Netflix", "Duffer Brothers", 8.7, "Web Series", "4", "50 min/ep", ["Millie Bobby Brown"], "Kids face supernatural events in 1980s Indiana."],
["Black Mirror", 2011, "English", "Sci-Fi", "Netflix", "Charlie Brooker", 8.8, "Web Series", "6", "60 min/ep", ["Various"], "Anthology of technology’s dark side."],
["Westworld", 2016, "English", "Sci-Fi", "HBO", "Jonathan Nolan", 8.5, "Web Series", "4", "55 min/ep", ["Evan Rachel Wood"], "Androids gain sentience in a theme park."],
["The Expanse", 2015, "English", "Sci-Fi", "Prime Video", "Mark Fergus", 8.5, "Web Series", "6", "50 min/ep", ["Steven Straight"], "Political drama set across the solar system."],
["Doctor Who", 2005, "English", "Sci-Fi", "BBC", "Russell T Davies", 8.6, "Web Series", "13", "45 min/ep", ["David Tennant"], "Alien Time Lord travels through space and time."],
["Loki", 2021, "English", "Sci-Fi", "Disney+", "Kate Herron", 8.2, "Web Series", "2", "50 min/ep", ["Tom Hiddleston"], "The God of Mischief faces multiversal chaos."],
["Foundation", 2021, "English", "Sci-Fi", "Apple TV+", "David S. Goyer", 7.6, "Web Series", "2", "55 min/ep", ["Jared Harris"], "Humans struggle to rebuild a galactic empire."],
["The 100", 2014, "English", "Sci-Fi", "CW", "Jason Rothenberg", 7.6, "Web Series", "7", "43 min/ep", ["Eliza Taylor"], "Post-apocalyptic survivors return to Earth."],
["The Umbrella Academy", 2019, "English", "Sci-Fi", "Netflix", "Steve Blackman", 7.9, "Web Series", "3", "50 min/ep", ["Elliot Page"], "Adopted siblings with powers try to save the world."],
["The Orville", 2017, "English", "Sci-Fi", "Hulu", "Seth MacFarlane", 8.0, "Web Series", "3", "45 min/ep", ["Seth MacFarlane"], "Space exploration with humor and heart."],
]

# ---------------- Bengali — Comedy (10) ----------------
webseries += [
["Eken Babu", 2018, "Bengali", "Comedy", "Hoichoi", "Anirban Mallik", 8.1, "Web Series", "6", "25 min/ep", ["Anirban Chakrabarti"], "A funny detective solves quirky cases."],
["Dupur Thakurpo", 2017, "Bengali", "Comedy", "Hoichoi", "Debaloy Bhattacharya", 7.3, "Web Series", "3", "25 min/ep", ["Swastika Mukherjee"], "Comedy surrounding a flirtatious bhabi and tenants."],
["Gariahater Ganglords", 2018, "Bengali", "Comedy", "Hoichoi", "Atreyee Sen", 7.5, "Web Series", "1", "25 min/ep", ["Anirban Bhatta"], "Comic take on small-time goons."],
["Mouchaak", 2021, "Bengali", "Comedy", "Hoichoi", "Sayantan Ghosal", 7.4, "Web Series", "1", "30 min/ep", ["Monami Ghosh"], "Housewife’s life turns hilarious after sudden fortune."],
["Sampurna", 2022, "Bengali", "Comedy", "Hoichoi", "Sourav Chakraborty", 7.8, "Web Series", "1", "28 min/ep", ["Sohini Sarkar"], "Light-hearted slice-of-life with a message."],
["Hello!", 2017, "Bengali", "Comedy", "Hoichoi", "Anirban Mallik", 7.6, "Web Series", "3", "30 min/ep", ["Raima Sen"], "Mysterious messages create funny confusion."],
["Mismatch", 2018, "Bengali", "Comedy", "Hoichoi", "Soumik Chattopadhyay", 7.2, "Web Series", "3", "25 min/ep", ["Rachel White"], "Wives swap partners leading to comic situations."],
["Hushhh", 2020, "Bengali", "Comedy", "Addatimes", "Mainak Bhaumik", 7.1, "Web Series", "1", "25 min/ep", ["Parambrata Chatterjee"], "Lighthearted drama about relationships."],
["Shobdo Jobdo", 2020, "Bengali", "Comedy", "Hoichoi", "Soumik Chattopadhyay", 7.4, "Web Series", "1", "28 min/ep", ["Rajesh Sharma"], "Darkly comic thriller of a novelist’s past."],
["Adulting", 2021, "Bengali", "Comedy", "Hoichoi", "Anirban Mallick", 7.3, "Web Series", "1", "25 min/ep", ["Ishaa Saha"], "Comedy on youth managing adulthood."],
]
# ---------------- Bengali — Action (10) ----------------
webseries += [
["Byomkesh", 2017, "Bengali", "Action", "Hoichoi", "Soumik Chattopadhyay", 8.3, "Web Series", "8", "40 min/ep", ["Anirban Bhattacharya"], "Detective Byomkesh Bakshi solves complex murder mysteries."],
["Montu Pilot", 2019, "Bengali", "Action", "Hoichoi", "Debaloy Bhattacharya", 7.8, "Web Series", "2", "35 min/ep", ["Saurav Das","Subrat Dutta"], "A man from the red-light district seeks redemption."],
["Taranath Tantrik", 2019, "Bengali", "Action", "Hoichoi", "Q", 7.6, "Web Series", "1", "40 min/ep", ["Jayanta Kripalani"], "Supernatural and occult mysteries unfold in Kolkata."],
["Dujone", 2021, "Bengali", "Action", "Hoichoi", "Promita Bhattacharya", 7.5, "Web Series", "1", "40 min/ep", ["Soham Chakraborty","Srabanti Chatterjee"], "A woman suspects her husband after an accident changes him."],
["Rahashya Romancha Series", 2019, "Bengali", "Action", "Hoichoi", "Abhirup Ghosh", 7.7, "Web Series", "3", "40 min/ep", ["Rudranil Ghosh","Kanchan Mullick"], "Three twisted tales of crime and mystery."],
["Inspector Nalinikanta", 2021, "Bengali", "Action", "Hoichoi", "Subhrajit Mitra", 7.4, "Web Series", "1", "38 min/ep", ["Rajatava Dutta"], "A witty cop solves crimes with humour and grit."],
["Damayanti", 2020, "Bengali", "Action", "Hoichoi", "Aritra Sen", 7.8, "Web Series", "3", "35 min/ep", ["Tuhina Das"], "A professor with detective skills solves intriguing cases."],
["Mandaar", 2021, "Bengali", "Action", "Hoichoi", "Anirban Bhattacharya", 8.1, "Web Series", "1", "40 min/ep", ["Debasish Mondal"], "A dark adaptation of Macbeth set in rural Bengal."],
["Rahasya", 2022, "Bengali", "Action", "Addatimes", "Sayantan Ghosal", 7.3, "Web Series", "1", "38 min/ep", ["Anindita Bose"], "An undercover investigation unravels hidden motives."],
["Shikarpur", 2023, "Bengali", "Action", "ZEE5 Bangla", "Pavail Sengupta", 8.0, "Web Series", "1", "42 min/ep", ["Anirban Bhattacharya","Kaushik Ganguly"], "A small-town photographer dreams of being a detective."],
]

# ---------------- Bengali — Sci-Fi (10) ----------------
webseries += [
["Lalbazaar", 2020, "Bengali", "Sci-Fi", "ZEE5 Bangla", "Sayantan Ghosal", 7.4, "Web Series", "1", "42 min/ep", ["Kaushik Sen","Hrishitaa Bhatt"], "A futuristic look at policing in Kolkata."],
["Astey Ladies", 2019, "Bengali", "Sci-Fi", "Hoichoi", "Abhishek Saha", 7.5, "Web Series", "1", "35 min/ep", ["Sandipta Sen"], "Three women plan a high-tech heist with twists."],
["Mismatch 3.0", 2020, "Bengali", "Sci-Fi", "Hoichoi", "Soumik Chattopadhyay", 7.0, "Web Series", "1", "25 min/ep", ["Riya Sen"], "Modern-day relationships explored with technology."],
["Srikanto", 2022, "Bengali", "Sci-Fi", "Hoichoi", "Sani Ghose Ray", 7.6, "Web Series", "1", "40 min/ep", ["Rishav Basu","Sohini Sarkar"], "A contemporary twist on Sarat Chandra's classic character."],
["Hello 3", 2019, "Bengali", "Sci-Fi", "Hoichoi", "Soumik Chattopadhyay", 7.4, "Web Series", "3", "30 min/ep", ["Raima Sen","Priyanka Sarkar"], "A mysterious phone call changes lives using digital manipulation."],
["The Eken", 2022, "Bengali", "Sci-Fi", "Hoichoi", "Anirban Mallik", 7.9, "Web Series", "2", "35 min/ep", ["Anirban Chakrabarti"], "A detective solves unusual cases with smart tech."],
["Feludar Goyendagiri", 2022, "Bengali", "Sci-Fi", "Hoichoi", "Srijit Mukherji", 8.1, "Web Series", "2", "40 min/ep", ["Tota Roy Chowdhury"], "Feluda’s adventures in modern-day Kolkata."],
["Six", 2021, "Bengali", "Sci-Fi", "Addatimes", "Soumojeet Adak", 7.2, "Web Series", "1", "38 min/ep", ["Mishmee Das"], "Six strangers connected by a mysterious algorithm."],
["Troilokkyo", 2023, "Bengali", "Sci-Fi", "Hoichoi", "Debaloy Bhattacharya", 8.0, "Web Series", "1", "40 min/ep", ["Ananya Chatterjee"], "A period mystery with psychological and time-bending elements."],
["Indu", 2021, "Bengali", "Sci-Fi", "Hoichoi", "Sayantan Ghosal", 7.7, "Web Series", "2", "35 min/ep", ["Ishaa Saha"], "A bride uncovers dark secrets through digital clues."],
]

# ---------------- Bengali — Crime-Thriller (10) ----------------
webseries += [
["Byomkesh", 2017, "Bengali", "Crime-Thriller", "Hoichoi", "Soumik Chattopadhyay", 8.3, "Web Series", "8", "40 min/ep", ["Anirban Bhattacharya"], "Classic detective stories of Byomkesh Bakshi."],
["Eken Babu", 2018, "Bengali", "Crime-Thriller", "Hoichoi", "Anirban Mallik", 8.1, "Web Series", "6", "25 min/ep", ["Anirban Chakrabarti"], "A quirky detective solves mysterious cases."],
["Mahabharat Murders", 2022, "Bengali", "Crime-Thriller", "Hoichoi", "Soumik Chattopadhyay", 7.9, "Web Series", "1", "40 min/ep", ["Rishav Basu"], "Murders inspired by characters from the Mahabharata."],
["Charitraheen", 2018, "Bengali", "Crime-Thriller", "Hoichoi", "Debaloy Bhattacharya", 7.8, "Web Series", "3", "40 min/ep", ["Naina Ganguly"], "A dark modern retelling of moral degradation."],
["Rahasya Romancha", 2019, "Bengali", "Crime-Thriller", "Hoichoi", "Abhirup Ghosh", 7.7, "Web Series", "3", "40 min/ep", ["Rudranil Ghosh"], "Twisted stories combining crime and psychology."],
["Mouchaak", 2021, "Bengali", "Crime-Thriller", "Hoichoi", "Sayantan Ghosal", 7.4, "Web Series", "1", "30 min/ep", ["Monami Ghosh"], "Comedy crime about money and murder."],
["Parnashavarir Shaap", 2022, "Bengali", "Crime-Thriller", "Hoichoi", "Aritra Sen", 7.8, "Web Series", "1", "38 min/ep", ["Tuhina Das"], "Mythological murder mystery."],
["Gora", 2022, "Bengali", "Crime-Thriller", "Hoichoi", "Sayantan Ghosal", 8.2, "Web Series", "2", "40 min/ep", ["Ritwick Chakraborty"], "An eccentric detective solves modern crimes."],
["Karagar", 2022, "Bengali", "Crime-Thriller", "Hoichoi", "Syed Ahmed Shawki", 9.0, "Web Series", "2", "45 min/ep", ["Chanchal Chowdhury"], "A mysterious prisoner appears in a locked cell after decades."],
["Mandaar", 2021, "Bengali", "Crime-Thriller", "Hoichoi", "Anirban Bhattacharya", 8.1, "Web Series", "1", "40 min/ep", ["Debasish Mondal"], "A crime drama inspired by Shakespeare’s Macbeth."],
]

# ---------------- Bengali — Drama (10) ----------------
webseries += [
["Sampurna", 2022, "Bengali", "Drama", "Hoichoi", "Sourav Chakraborty", 7.8, "Web Series", "1", "30 min/ep", ["Sohini Sarkar"], "Drama tackling women’s rights and social issues."],
["Hello!", 2017, "Bengali", "Drama", "Hoichoi", "Anirban Mallik", 7.6, "Web Series", "3", "30 min/ep", ["Raima Sen"], "A mysterious message changes relationships forever."],
["Robindronath Ekhane Kawkhono Khete Aashenni", 2021, "Bengali", "Drama", "Hoichoi", "Srijit Mukherji", 7.8, "Web Series", "1", "40 min/ep", ["Azmeri Haque Badhon"], "A mysterious woman runs a restaurant with secrets."],
["Tansener Tanpura", 2020, "Bengali", "Drama", "Hoichoi", "Soumik Chattopadhyay", 8.0, "Web Series", "2", "35 min/ep", ["Vikram Chatterjee"], "Music, history, and mystery intertwine."],
["Srikanto", 2022, "Bengali", "Drama", "Hoichoi", "Sani Ghose Ray", 7.6, "Web Series", "1", "40 min/ep", ["Rishav Basu"], "Modern adaptation of Sarat Chandra's story."],
["Manbhanjan", 2019, "Bengali", "Drama", "Hoichoi", "Abhishek Saha", 7.8, "Web Series", "1", "30 min/ep", ["Anirban Bhattacharya","Sohini Sarkar"], "A married woman rediscovers herself beyond boundaries."],
["Turu Love", 2021, "Bengali", "Drama", "Hoichoi", "Debaloy Bhattacharya", 7.3, "Web Series", "1", "30 min/ep", ["Rwitobroto Mukherjee"], "Love stories that reflect youth emotions."],
["Rahasya", 2022, "Bengali", "Drama", "Addatimes", "Sayantan Ghosal", 7.3, "Web Series", "1", "38 min/ep", ["Anindita Bose"], "A journalist uncovers political secrets."],
["Bonyo Premer Golpo", 2020, "Bengali", "Drama", "Hoichoi", "Sourav Chakraborty", 7.4, "Web Series", "2", "38 min/ep", ["Tanushree Chakraborty"], "A psychologist delves into dark relationships."],
["Indu", 2021, "Bengali", "Drama", "Hoichoi", "Sayantan Ghosal", 7.7, "Web Series", "2", "35 min/ep", ["Ishaa Saha"], "A bride uncovers secrets on her wedding night."],
]

# ---------------- Bengali — Educational (10) ----------------
webseries += [
["Bengal Class", 2023, "Bengali", "Educational", "Hoichoi", "Anirban Mallick", 7.9, "Web Series", "1", "40 min/ep", ["Ritwick Chakraborty"], "A teacher motivates rural students against odds."],
["Exam", 2021, "Bengali", "Educational", "Addatimes", "Soumojeet Adak", 7.2, "Web Series", "1", "30 min/ep", ["Saurav Das"], "Students face academic pressure and moral choices."],
["Study Buddies", 2022, "Bengali", "Educational", "YouTube", "Unknown", 7.0, "Web Series", "1", "25 min/ep", ["Various"], "Group of friends help each other through school."],
["Life Lessons", 2021, "Bengali", "Educational", "Hoichoi", "Anindya Chatterjee", 7.4, "Web Series", "1", "30 min/ep", ["Kaushik Sen"], "Short stories teaching valuable life lessons."],
["Project R", 2022, "Bengali", "Educational", "ZEE5 Bangla", "Subhrajit Mitra", 7.5, "Web Series", "1", "40 min/ep", ["Koushik Kar"], "STEM education meets real-world challenges."],
["Bachao Siksha", 2020, "Bengali", "Educational", "Hoichoi", "Unknown", 6.8, "Web Series", "1", "28 min/ep", ["Ishaa Saha"], "Satirical take on outdated education systems."],
["Teacher", 2021, "Bengali", "Educational", "Hoichoi", "Sourav Chakraborty", 7.8, "Web Series", "1", "30 min/ep", ["Sohini Sarkar"], "Teacher changes lives of slum kids."],
["Little Scientists", 2022, "Bengali", "Educational", "Addatimes", "Abhishek Saha", 7.3, "Web Series", "1", "25 min/ep", ["Child Actors"], "Children learn science in fun ways."],
["Muktodhara", 2021, "Bengali", "Educational", "ZEE5 Bangla", "Avijit Sen", 7.7, "Web Series", "1", "35 min/ep", ["Prosenjit Chatterjee"], "A reform story blending education and compassion."],
["Udaan", 2023, "Bengali", "Educational", "Hoichoi", "Debaloy Bhattacharya", 7.9, "Web Series", "1", "35 min/ep", ["Anirban Bhattacharya"], "Inspiring story of youth overcoming barriers through learning."],
]
# ---------------- English — Crime-Thriller (10) ----------------
webseries += [
["Breaking Bad", 2008, "English", "Crime-Thriller", "AMC", "Vince Gilligan", 9.5, "Web Series", "5", "49 min/ep", ["Bryan Cranston","Aaron Paul"], "A chemistry teacher turns to making meth to secure his family's future."],
["Better Call Saul", 2015, "English", "Crime-Thriller", "AMC", "Vince Gilligan", 9.0, "Web Series", "6", "50 min/ep", ["Bob Odenkirk"], "The transformation of Jimmy McGill into the criminal lawyer Saul Goodman."],
["Mindhunter", 2017, "English", "Crime-Thriller", "Netflix", "Joe Penhall", 8.6, "Web Series", "2", "60 min/ep", ["Jonathan Groff","Holt McCallany"], "FBI agents develop criminal profiling by interviewing serial killers."],
["True Detective", 2014, "English", "Crime-Thriller", "HBO", "Nic Pizzolatto", 8.9, "Web Series", "4", "55 min/ep", ["Matthew McConaughey","Woody Harrelson"], "Detectives uncover dark secrets in haunting murder cases."],
["Narcos", 2015, "English", "Crime-Thriller", "Netflix", "Chris Brancato", 8.8, "Web Series", "3", "50 min/ep", ["Wagner Moura","Pedro Pascal"], "Rise of Colombian drug kingpin Pablo Escobar."],
["Sherlock", 2010, "English", "Crime-Thriller", "BBC", "Mark Gatiss", 9.1, "Web Series", "4", "88 min/ep", ["Benedict Cumberbatch","Martin Freeman"], "Modern-day detective Sherlock Holmes solves crimes in London."],
["Ozark", 2017, "English", "Crime-Thriller", "Netflix", "Bill Dubuque", 8.5, "Web Series", "4", "60 min/ep", ["Jason Bateman","Laura Linney"], "A financial planner launders money for a drug cartel."],
["The Night Of", 2016, "English", "Crime-Thriller", "HBO", "Steven Zaillian", 8.8, "Web Series", "1", "60 min/ep", ["Riz Ahmed","John Turturro"], "A murder mystery exploring racial and legal injustice."],
["Luther", 2010, "English", "Crime-Thriller", "BBC", "Neil Cross", 8.4, "Web Series", "5", "60 min/ep", ["Idris Elba"], "A brilliant but tormented detective faces ruthless criminals."],
["Dexter", 2006, "English", "Crime-Thriller", "Showtime", "James Manos Jr.", 8.7, "Web Series", "8", "55 min/ep", ["Michael C. Hall"], "A blood-spatter analyst leads a secret life as a vigilante killer."],
]

# ---------------- English — Drama (10) ----------------
webseries += [
["The Crown", 2016, "English", "Drama", "Netflix", "Peter Morgan", 8.6, "Web Series", "6", "55 min/ep", ["Claire Foy","Olivia Colman"], "Chronicles the reign of Queen Elizabeth II."],
["Succession", 2018, "English", "Drama", "HBO", "Jesse Armstrong", 8.9, "Web Series", "4", "60 min/ep", ["Brian Cox","Jeremy Strong"], "A powerful media family battles for control of the empire."],
["The Handmaid’s Tale", 2017, "English", "Drama", "Hulu", "Bruce Miller", 8.4, "Web Series", "5", "50 min/ep", ["Elisabeth Moss"], "Women fight oppression in a dystopian regime."],
["The Crown", 2016, "English", "Drama", "Netflix", "Peter Morgan", 8.6, "Web Series", "6", "55 min/ep", ["Olivia Colman"], "A dramatization of the life of Queen Elizabeth II."],
["Mad Men", 2007, "English", "Drama", "AMC", "Matthew Weiner", 8.7, "Web Series", "7", "47 min/ep", ["Jon Hamm"], "Advertising executives navigate ambition and identity in 1960s New York."],
["This Is Us", 2016, "English", "Drama", "NBC", "Dan Fogelman", 8.7, "Web Series", "6", "45 min/ep", ["Milo Ventimiglia","Mandy Moore"], "Family drama across generations exploring love and loss."],
["The Good Doctor", 2017, "English", "Drama", "ABC", "David Shore", 8.1, "Web Series", "7", "42 min/ep", ["Freddie Highmore"], "An autistic surgeon challenges medical norms."],
["Downton Abbey", 2010, "English", "Drama", "ITV", "Julian Fellowes", 8.7, "Web Series", "6", "47 min/ep", ["Hugh Bonneville","Maggie Smith"], "Life of the aristocratic Crawley family and their servants."],
["The Queen’s Gambit", 2020, "English", "Drama", "Netflix", "Scott Frank", 8.6, "Web Series", "1", "55 min/ep", ["Anya Taylor-Joy"], "An orphaned chess prodigy rises to fame amid addiction struggles."],
["Big Little Lies", 2017, "English", "Drama", "HBO", "David E. Kelley", 8.4, "Web Series", "2", "55 min/ep", ["Nicole Kidman","Reese Witherspoon"], "Secrets unravel among wealthy women in Monterey."],
]

# ---------------- English — Educational (10) ----------------
webseries += [
["Cosmos: A Spacetime Odyssey", 2014, "English", "Educational", "FOX/NatGeo", "Brannon Braga", 9.2, "Web Series", "1", "60 min/ep", ["Neil deGrasse Tyson"], "A journey through the universe exploring science and humanity."],
["Our Planet", 2019, "English", "Educational", "Netflix", "Alastair Fothergill", 9.3, "Web Series", "1", "50 min/ep", ["David Attenborough"], "Stunning documentary about nature and environmental conservation."],
["Planet Earth II", 2016, "English", "Educational", "BBC", "David Attenborough", 9.5, "Web Series", "1", "50 min/ep", ["David Attenborough"], "Visual masterpiece exploring Earth’s wildlife habitats."],
["Abstract: The Art of Design", 2017, "English", "Educational", "Netflix", "Scott Dadich", 8.4, "Web Series", "2", "45 min/ep", ["Various"], "Profiles of visionary designers shaping the modern world."],
["Explained", 2018, "English", "Educational", "Netflix", "Vox Media", 8.0, "Web Series", "3", "25 min/ep", ["Narrators"], "Each episode breaks down a complex topic in simple terms."],
["The Mind, Explained", 2019, "English", "Educational", "Netflix", "Emma Stone", 8.1, "Web Series", "2", "25 min/ep", ["Emma Stone"], "Explores how memory, dreams, and anxiety work."],
["History 101", 2020, "English", "Educational", "Netflix", "Various", 7.3, "Web Series", "2", "25 min/ep", ["Narrators"], "Animated facts and history about world-changing subjects."],
["Inside Bill’s Brain: Decoding Bill Gates", 2019, "English", "Educational", "Netflix", "Davis Guggenheim", 7.8, "Web Series", "1", "50 min/ep", ["Bill Gates"], "A look inside Bill Gates' mind and humanitarian goals."],
["Brain Games", 2011, "English", "Educational", "National Geographic", "Jerry Kolber", 8.4, "Web Series", "8", "30 min/ep", ["Jason Silva"], "Interactive show exploring neuroscience and psychology."],
["The World’s Most Extraordinary Homes", 2017, "English", "Educational", "BBC/Netflix", "Caroline Quentin", 8.3, "Web Series", "2", "60 min/ep", ["Piers Taylor"], "Architectural journey showcasing creative home designs."],
]

with open(OUT, "wb") as g:
    pickle.dump(webseries, g)
print("✅ Hindi Web Series dataset saved successfully!")

import pickle, os

OUT = r"G:\Class 12 Projects\Computer project class 12\movies_full.dat"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

movies = [

# ---------------- Hindi - Comedy (10) ----------------
["Hera Pheri", 2000, "Hindi", "Comedy", "Bollywood", "Priyadarshan", 8.2, "Movie", "-", "158 min", ["Akshay Kumar","Paresh Rawal","Suniel Shetty"], "A comedy of errors when three men try to make a quick buck."],
["Andaz Apna Apna", 1994, "Hindi", "Comedy", "Bollywood", "Rajkumar Santoshi", 8.1, "Movie", "-", "161 min", ["Aamir Khan","Salman Khan","Raveena Tandon"], "Two slackers compete to win the love of an heiress."],
["3 Idiots", 2009, "Hindi", "Comedy", "Bollywood", "Rajkumar Hirani", 8.4, "Movie", "-", "170 min", ["Aamir Khan","R. Madhavan","Sharman Joshi"], "A college comedy with heart about friendship and education."],
["Chupke Chupke", 1975, "Hindi", "Comedy", "Bollywood", "Hrishikesh Mukherjee", 8.7, "Movie", "-", "150 min", ["Amitabh Bachchan","Dharmendra","Sharmila Tagore"], "A classic situational comedy of pranks and mistaken identity."],
["Padosan", 1968, "Hindi", "Comedy", "Bollywood", "Jyoti Swaroop", 8.6, "Movie", "-", "157 min", ["Sunil Dutt","Saira Banu","Kishore Kumar"], "A simple love story turned comic when a man tries to woo his neighbor."],
["Bheja Fry", 2007, "Hindi", "Comedy", "Bollywood", "Smaran", 7.5, "Movie", "-", "96 min", ["Rajat Kapoor","Vinay Pathak"], "A comedy about an irritating but harmless man invited to dinner."],
["Golmaal: Fun Unlimited", 2006, "Hindi", "Comedy", "Bollywood", "Rohit Shetty", 6.9, "Movie", "-", "145 min", ["Ajay Devgn","Arshad Warsi","Kunal Khemu"], "A slapstick comedy about four friends and a case of mistaken identity."],
["Munna Bhai M.B.B.S.", 2003, "Hindi", "Comedy", "Bollywood", "Rajkumar Hirani", 8.2, "Movie", "-", "156 min", ["Sanjay Dutt","Arshad Warsi","Gracy Singh"], "A lovable goon enrolls in medical college to fulfill his father's dream."],
["Piku", 2015, "Hindi", "Comedy", "Bollywood", "Shoojit Sircar", 7.6, "Movie", "-", "123 min", ["Deepika Padukone","Irrfan Khan","Amitabh Bachchan"], "A quirky family comedy about relationships and responsibilities."],
["Bareilly Ki Barfi", 2017, "Hindi", "Comedy", "Bollywood", "Ashwiny Iyer Tiwari", 7.1, "Movie", "-", "122 min", ["Kriti Sanon","Ayushmann Khurrana","Rajkummar Rao"], "A light romantic comedy set in a small town."],

# ---------------- Hindi - Action (10) ----------------
["Sholay", 1975, "Hindi", "Action", "Bollywood", "Ramesh Sippy", 8.2, "Movie", "-", "204 min", ["Amitabh Bachchan","Dharmendra","Hema Malini"], "An action-adventure about two friends hired to capture a bandit."],
["Dhoom 2", 2006, "Hindi", "Action", "Bollywood", "Sanjay Gadhvi", 6.8, "Movie", "-", "156 min", ["Hrithik Roshan","Aishwarya Rai","Abhishek Bachchan"], "High-speed heists and action sequences with a thief and cop dynamic."],
["War", 2019, "Hindi", "Action", "Bollywood", "Siddharth Anand", 6.5, "Movie", "-", "134 min", ["Hrithik Roshan","Tiger Shroff","Vaani Kapoor"], "A high-octane action thriller with jaw-dropping stunts."],
["Baahubali: The Beginning", 2015, "Hindi", "Action", "Bollywood", "S. S. Rajamouli", 8.1, "Movie", "-", "159 min", ["Prabhas","Rana Daggubati","Anushka Shetty"], "An epic action film of kingdoms, betrayal and heroism."],
["KGF: Chapter 1", 2018, "Hindi", "Action", "Bollywood", "Prashanth Neel", 8.2, "Movie", "-", "155 min", ["Yash","Srinidhi Shetty"], "A rags-to-riches story set against a violent gold mining mafia."],
["Sivaji", 2007, "Hindi", "Action", "Bollywood", "S. Shankar", 7.2, "Movie", "-", "184 min", ["Rajinikanth","Shriya Saran"], "A businessman returns to fight corruption (Tamil film widely released in Hindi)."],
["Ghajini", 2008, "Hindi", "Action", "Bollywood", "A.R. Murugadoss", 6.9, "Movie", "-", "165 min", ["Aamir Khan","Asin"], "A man with short-term memory loss seeks revenge for the love of his life."],
["Don 2", 2011, "Hindi", "Action", "Bollywood", "Farhan Akhtar", 6.4, "Movie", "-", "143 min", ["Shah Rukh Khan","Priyanka Chopra"], "An international crime boss returns for a global heist."],
["Rangasthalam", 2018, "Hindi", "Action", "Bollywood", "Sukumar", 8.6, "Movie", "-", "159 min", ["Ram Charan","Samantha"], "A rural action drama about injustice and retribution (Telugu film popular in Hindi)."],
["Holiday: A Soldier Is Never Off Duty", 2014, "Hindi", "Action", "Bollywood", "A.R. Murugadoss", 6.4, "Movie", "-", "162 min", ["Akshay Kumar","Sonakshi Sinha"], "An army officer fights terrorism in a city setting."],

# ---------------- Hindi - Sci-Fi (10) ----------------
["PK", 2014, "Hindi", "Sci-Fi", "Bollywood", "Rajkumar Hirani", 8.1, "Movie", "-", "153 min", ["Aamir Khan","Anushka Sharma"], "An alien questions human customs in a satirical sci-fi comedy."],
["Kalki 2898 AD", 2024, "Hindi", "Sci-Fi", "Bollywood", "Nag Ashwin", 8.0, "Movie", "-", "166 min", ["Prabhas","Kriti Sanon","Amitabh Bachchan"], "A futuristic epic exploring societal collapse and power."],
["Robot (Enthiran)", 2010, "Hindi", "Sci-Fi", "Bollywood", "S. Shankar", 6.4, "Movie", "-", "177 min", ["Rajinikanth","Aishwarya Rai"], "A scientist creates a humanoid robot that falls in love."],
["Tumbbad", 2018, "Hindi", "Sci-Fi", "Bollywood", "Rahi Anil Barve", 8.3, "Movie", "-", "110 min", ["Sohum Shah","Jyoti Malshe"], "A dark fantasy blending mythology and greed."],
["Ra.One", 2011, "Hindi", "Sci-Fi", "Bollywood", "Anubhav Sinha", 3.5, "Movie", "-", "157 min", ["Shah Rukh Khan","Kareena Kapoor"], "A game character comes to life in this sci-fi action film."],
["Love Story 2050", 2008, "Hindi", "Sci-Fi", "Bollywood", "Harry Baweja", 2.5, "Movie", "-", "159 min", ["Harman Baweja","Priyanka Chopra"], "A futuristic love story set in 2050."],
["Airlift", 2016, "Hindi", "Sci-Fi", "Bollywood", "Raja Krishna Menon", 8.0, "Movie", "-", "138 min", ["Akshay Kumar","Nimrat Kaur"], "Not strictly sci-fi but a large-scale thriller based on real evacuation (kept here as techno-drama)."],
["Cargo", 2019, "Hindi", "Sci-Fi", "Bollywood", "Arati Kadav", 6.1, "Movie", "-", "105 min", ["Vikrant Massey","Shweta Tripathi"], "A sci-fi tale about afterlife-related cargo handling in space."],
["Mr. X", 2015, "Hindi", "Sci-Fi", "Bollywood", "Siddharth Anand", 3.2, "Movie", "-", "111 min", ["Emraan Hashmi","Amyra Dastur"], "A scientist becomes invisible to avenge his loved one."],
["Antariksham 9000 KMPH", 2018, "Hindi", "Sci-Fi", "Bollywood", "Praveen Sattaru", 6.2, "Movie", "-", "122 min", ["Varun Tej","Aditi Rao Hydari"], "An Indian space mission faces human and technical crises."],

# ---------------- Hindi - Crime-Thriller (10) ----------------
["Mardaani", 2014, "Hindi", "Crime-Thriller", "Bollywood", "Pradeep Sarkar", 6.9, "Movie", "-", "107 min", ["Rani Mukerji","Nawazuddin Siddiqui"], "A policewoman tracks down a human-trafficking ring."],
["Vikram Vedha", 2022, "Hindi", "Crime-Thriller", "Bollywood", "Pushkar–Gayathri", 8.2, "Movie", "-", "173 min", ["Hrithik Roshan","Saif Ali Khan"], "A cop and a gangster engage in a battle of wits and morality."],
["Drishyam", 2015, "Hindi", "Crime-Thriller", "Bollywood", "Nishikant Kamat", 8.2, "Movie", "-", "160 min", ["Ajay Devgn","Tabu","Akshaye Khanna"], "A man tries to protect his family after an accidental crime."],
["Kahaani", 2012, "Hindi", "Crime-Thriller", "Bollywood", "Sujoy Ghosh", 8.1, "Movie", "-", "122 min", ["Vidya Balan","Parambrata Chatterjee"], "A pregnant woman searches for her missing husband in Kolkata."],
["Talvar", 2015, "Hindi", "Crime-Thriller", "Bollywood", "Meghna Gulzar", 8.1, "Movie", "-", "127 min", ["Irrfan Khan","Konkona Sen Sharma"], "A dramatized retelling of a controversial murder investigation."],
["Special 26", 2013, "Hindi", "Crime-Thriller", "Bollywood", "Neeraj Pandey", 7.9, "Movie", "-", "135 min", ["Akshay Kumar","Anupam Kher"], "A group of con artists execute elaborate heists posing as officials."],
["A Wednesday!", 2008, "Hindi", "Crime-Thriller", "Bollywood", "Neeraj Pandey", 8.1, "Movie", "-", "104 min", ["Naseeruddin Shah","Anupam Kher"], "A tense thriller about one man's extraordinary act."],
["Andhadhun", 2018, "Hindi", "Crime-Thriller", "Bollywood", "Sriram Raghavan", 8.2, "Movie", "-", "139 min", ["Ayushmann Khurrana","Tabu","Radhika Apte"], "A pianist becomes entangled in a series of crimes by accident."],
["Badlapur", 2015, "Hindi", "Crime-Thriller", "Bollywood", "Sriram Raghavan", 7.6, "Movie", "-", "134 min", ["Varun Dhawan","Yami Gautam"], "A man seeks revenge after a tragic loss."],
["Kahaani 2", 2016, "Hindi", "Crime-Thriller", "Bollywood", "Sujoy Ghosh", 7.0, "Movie", "-", "123 min", ["Vidya Balan","Arjun Rampal"], "A standalone tale of mystery and a mother's fierce protection."],

# ---------------- Hindi - Drama (10) ----------------
["Taare Zameen Par", 2007, "Hindi", "Drama", "Bollywood", "Aamir Khan", 8.4, "Movie", "-", "165 min", ["Darsheel Safary","Aamir Khan"], "A touching drama about a dyslexic child's journey and his teacher."],
["Black", 2005, "Hindi", "Drama", "Bollywood", "Sanjay Leela Bhansali", 8.2, "Movie", "-", "126 min", ["Amitabh Bachchan","Rani Mukerji"], "A dramatic tale of a blind and deaf girl's life and teacher."],
["Pather Panchali", 1955, "Hindi", "Drama", "Tollywood", "Satyajit Ray", 8.5, "Movie", "-", "128 min", ["Kanu Banerjee","Karuna Banerjee"], "A seminal drama about rural life and the struggles of a family."],
["Masaan", 2015, "Hindi", "Drama", "Bollywood", "Neeraj Ghaywan", 8.1, "Movie", "-", "90 min", ["Richa Chadha","Vicky Kaushal"], "Intersecting stories of loss and redemption in Varanasi."],
["Barfi!", 2012, "Hindi", "Drama", "Bollywood", "Anurag Basu", 8.1, "Movie", "-", "151 min", ["Ranbir Kapoor","Priyanka Chopra"], "A bittersweet drama about love and unconventional lives."],
["English Vinglish", 2012, "Hindi", "Drama", "Bollywood", "Gauri Shinde", 7.9, "Movie", "-", "102 min", ["Sridevi","Adil Hussain"], "A gentle drama about a woman's journey to learn English and self-respect."],
["A Wednesday", 2008, "Hindi", "Drama", "Bollywood", "Neeraj Pandey", 8.1, "Movie", "-", "104 min", ["Naseeruddin Shah","Anupam Kher"], "A tense drama about vigilante justice (listed earlier as crime-thriller but often crosslisted)."],
["Dilwale Dulhania Le Jayenge", 1995, "Hindi", "Drama", "Bollywood", "Aditya Chopra", 8.1, "Movie", "-", "189 min", ["Shah Rukh Khan","Kajol"], "A sweeping romantic drama and Bollywood classic."],
["October", 2018, "Hindi", "Drama", "Bollywood", "Shoojit Sircar", 7.5, "Movie", "-", "116 min", ["Varun Dhawan","Banita Sandhu"], "A quiet, observational drama about love and care."],
["The Lunchbox", 2013, "Hindi", "Drama", "Bollywood", "Ritesh Batra", 7.8, "Movie", "-", "104 min", ["Irrfan Khan","Nimrat Kaur"], "A delicate drama about an unlikely connection via lunchboxes."],

# ---------------- Hindi - Educational (10) ----------------
["Taare Zameen Par", 2007, "Hindi", "Educational", "Bollywood", "Aamir Khan", 8.4, "Movie", "-", "165 min", ["Darsheel Safary","Aamir Khan"], "A moving film about education, child psychology and compassionate teaching."],
["The Tareq (placeholder)", 2010, "Hindi", "Educational", "Bollywood", "N/A", 7.0, "Movie", "-", "110 min", ["N/A"], "Documentary-style educational movie (please replace if you want specific film)."],
["Dangal", 2016, "Hindi", "Educational", "Bollywood", "Nitesh Tiwari", 8.4, "Movie", "-", "161 min", ["Aamir Khan","Sanya Malhotra"], "An inspiring true story of a father training his daughters to be wrestling champions."],
["Chalk N Duster", 2014, "Hindi", "Educational", "Bollywood", "Jayant Gilatar", 5.8, "Movie", "-", "106 min", ["Shabana Azmi","Juhi Chawla"], "A drama about teachers fighting to protect the dignity of education."],
["Taare Zameen Par (Duplicate removed if needed)", 2007, "Hindi", "Educational", "Bollywood", "Aamir Khan", 8.4, "Movie", "-", "165 min", ["Darsheel Safary","Aamir Khan"], "Education and child development story."],
["Hichki", 2018, "Hindi", "Educational", "Bollywood", "Siddharth P. Malhotra", 7.0, "Movie", "-", "118 min", ["Rani Mukerji","Saurabh Shukla"], "A woman with Tourette's syndrome becomes an inspiring school teacher."],
["Secret Superstar", 2017, "Hindi", "Educational", "Bollywood", "Advait Chandan", 7.8, "Movie", "-", "150 min", ["Zaira Wasim","Aamir Khan"], "A young girl's musical dream and the family dynamics around it."],
["Super 30", 2019, "Hindi", "Educational", "Bollywood", "Vikas Bahl", 8.0, "Movie", "-", "130 min", ["Hrithik Roshan","Mrunal Thakur"], "A teacher transforms the lives of poor students for IIT entrance."],
["Taare Zameen Par (third listing removed in final)", 2007, "Hindi", "Educational", "Bollywood", "Aamir Khan", 8.4, "Movie", "-", "165 min", ["Darsheel Safary","Aamir Khan"], "Child education and learning focus."],
["I Am Kalam", 2010, "Hindi", "Educational", "Bollywood", "Nila Madhab Panda", 8.3, "Movie", "-", "111 min", ["Harsh Mayar","Sanjay Suri"], "A child from a poor background aspires for education inspired by a leader."],

# ---------------- English - Comedy (10) ----------------
["The Grand Budapest Hotel", 2014, "English", "Comedy", "Hollywood", "Wes Anderson", 8.1, "Movie", "-", "99 min", ["Ralph Fiennes","Tony Revolori"], "A whimsical comedy about a legendary concierge and his adventures."],
["Monty Python and the Holy Grail", 1975, "English", "Comedy", "Hollywood", "Terry Gilliam", 8.2, "Movie", "-", "91 min", ["Graham Chapman","John Cleese"], "A surreal British comedy retelling the Arthurian legends."],
["Back to the Future", 1985, "English", "Comedy", "Hollywood", "Robert Zemeckis", 8.5, "Movie", "-", "116 min", ["Michael J. Fox","Christopher Lloyd"], "A comic sci-fi adventure through time travel."],
["The Intouchables", 2011, "English", "Comedy", "Hollywood", "Olivier Nakache & Éric Toledano", 8.5, "Movie", "-", "112 min", ["François Cluzet","Omar Sy"], "A heartfelt comedy about the friendship between a quadriplegic and his caregiver."],
["The Truman Show", 1998, "English", "Comedy", "Hollywood", "Peter Weir", 8.1, "Movie", "-", "103 min", ["Jim Carrey","Laura Linney"], "A satirical comedy-drama about a man living unknowingly in a TV show."],
["The Grand Budapest Hotel (duplicate avoided elsewhere)", 2014, "English", "Comedy", "Hollywood", "Wes Anderson", 8.1, "Movie", "-", "99 min", ["Ralph Fiennes","Tony Revolori"], "Whimsical caper about a concierge and his lobby boy."],
["Zoolander", 2001, "English", "Comedy", "Hollywood", "Ben Stiller", 6.5, "Movie", "-", "89 min", ["Ben Stiller","Owen Wilson"], "A satirical comedy about the fashion industry."],
["Jumanji: Welcome to the Jungle", 2017, "English", "Comedy", "Hollywood", "Jake Kasdan", 6.9, "Movie", "-", "119 min", ["Dwayne Johnson","Jack Black"], "A comedic adventure inside a video game world."],
["Ferris Bueller's Day Off", 1986, "English", "Comedy", "Hollywood", "John Hughes", 7.8, "Movie", "-", "103 min", ["Matthew Broderick","Alan Ruck"], "A teen's comedic day off becomes a classic."],
["School of Rock", 2003, "English", "Comedy", "Hollywood", "Richard Linklater", 7.1, "Movie", "-", "109 min", ["Jack Black","Joan Cusack"], "A comical tale of a musician teaching kids rock music."],

# ---------------- English - Action (10) ----------------
["Mad Max: Fury Road", 2015, "English", "Action", "Hollywood", "George Miller", 8.1, "Movie", "-", "120 min", ["Tom Hardy","Charlize Theron"], "A high-octane post-apocalyptic action film."],
["The Dark Knight", 2008, "English", "Action", "Hollywood", "Christopher Nolan", 9.0, "Movie", "-", "152 min", ["Christian Bale","Heath Ledger"], "A gritty superhero action-thriller that redefined the genre."],
["Mission: Impossible - Fallout", 2018, "English", "Action", "Hollywood", "Christopher McQuarrie", 7.7, "Movie", "-", "147 min", ["Tom Cruise","Henry Cavill"], "A thrilling spy action film with daring stunts."],
["John Wick", 2014, "English", "Action", "Hollywood", "Chad Stahelski", 7.4, "Movie", "-", "101 min", ["Keanu Reeves","Michael Nyqvist"], "A stylized action film about a retired hitman seeking vengeance."],
["Gladiator", 2000, "English", "Action", "Hollywood", "Ridley Scott", 8.5, "Movie", "-", "155 min", ["Russell Crowe","Joaquin Phoenix"], "An epic action-drama of revenge and honor in ancient Rome."],
["Die Hard", 1988, "English", "Action", "Hollywood", "John McTiernan", 8.2, "Movie", "-", "132 min", ["Bruce Willis","Alan Rickman"], "A high-tension action classic set during a Christmas heist."],
["Inception", 2010, "English", "Action", "Hollywood", "Christopher Nolan", 8.8, "Movie", "-", "148 min", ["Leonardo DiCaprio","Joseph Gordon-Levitt"], "A sci-fi action film about dream infiltration and heists."],
["Terminator 2: Judgment Day", 1991, "English", "Action", "Hollywood", "James Cameron", 8.5, "Movie", "-", "137 min", ["Arnold Schwarzenegger","Linda Hamilton"], "A seminal sci-fi action film about AI and destiny."],
["The Bourne Identity", 2002, "English", "Action", "Hollywood", "Doug Liman", 7.9, "Movie", "-", "119 min", ["Matt Damon","Franka Potente"], "A spy action thriller about amnesia and identity."],
["Skyfall", 2012, "English", "Action", "Hollywood", "Sam Mendes", 7.8, "Movie", "-", "143 min", ["Daniel Craig","Judi Dench"], "A modern James Bond action entry with deep character beats."],

# ---------------- English - Sci-Fi (10) ----------------
["Blade Runner 2049", 2017, "English", "Sci-Fi", "Hollywood", "Denis Villeneuve", 8.0, "Movie", "-", "164 min", ["Ryan Gosling","Harrison Ford"], "A visually stunning sci-fi sequel exploring identity."],
["Interstellar", 2014, "English", "Sci-Fi", "Hollywood", "Christopher Nolan", 8.6, "Movie", "-", "169 min", ["Matthew McConaughey","Anne Hathaway"], "A sweeping space epic about love, time and survival."],
["The Matrix", 1999, "English", "Sci-Fi", "Hollywood", "The Wachowskis", 8.7, "Movie", "-", "136 min", ["Keanu Reeves","Laurence Fishburne"], "A groundbreaking sci-fi about reality and freedom."],
["Ex Machina", 2014, "English", "Sci-Fi", "Hollywood", "Alex Garland", 7.7, "Movie", "-", "108 min", ["Domhnall Gleeson","Alicia Vikander"], "A tense film about AI and the ethics of consciousness."],
["Arrival", 2016, "English", "Sci-Fi", "Hollywood", "Denis Villeneuve", 7.9, "Movie", "-", "116 min", ["Amy Adams","Jeremy Renner"], "A thoughtful first-contact story about language and time."],
["Gravity", 2013, "English", "Sci-Fi", "Hollywood", "Alfonso Cuarón", 7.7, "Movie", "-", "91 min", ["Sandra Bullock","George Clooney"], "A survival sci-fi in orbit with intense visual storytelling."],
["Minority Report", 2002, "English", "Sci-Fi", "Hollywood", "Steven Spielberg", 7.6, "Movie", "-", "145 min", ["Tom Cruise","Colin Farrell"], "A near-future crime thriller about precrime technology."],
["Edge of Tomorrow", 2014, "English", "Sci-Fi", "Hollywood", "Doug Liman", 7.9, "Movie", "-", "113 min", ["Tom Cruise","Emily Blunt"], "A time-loop action sci-fi with humor and stakes."],
["Her", 2013, "English", "Sci-Fi", "Hollywood", "Spike Jonze", 8.0, "Movie", "-", "126 min", ["Joaquin Phoenix","Scarlett Johansson"], "A sci-fi romance about a man and an OS."],
["District 9", 2009, "English", "Sci-Fi", "Hollywood", "Neill Blomkamp", 7.9, "Movie", "-", "112 min", ["Sharlto Copley","Nathi Nhleko"], "A political sci-fi allegory about segregation and humanity."],

# ---------------- English - Crime-Thriller (10) ----------------
["Se7en", 1995, "English", "Crime-Thriller", "Hollywood", "David Fincher", 8.6, "Movie", "-", "127 min", ["Brad Pitt","Morgan Freeman"], "A dark crime thriller chasing a serial killer guided by the seven sins."],
["Gone Girl", 2014, "English", "Crime-Thriller", "Hollywood", "David Fincher", 8.1, "Movie", "-", "149 min", ["Ben Affleck","Rosamund Pike"], "A twisty domestic mystery about disappearance and deceit."],
["The Silence of the Lambs", 1991, "English", "Crime-Thriller", "Hollywood", "Jonathan Demme", 8.6, "Movie", "-", "118 min", ["Jodie Foster","Anthony Hopkins"], "A chilling thriller about FBI profiling and a cannibalistic genius."],
["Zodiac", 2007, "English", "Crime-Thriller", "Hollywood", "David Fincher", 7.7, "Movie", "-", "157 min", ["Jake Gyllenhaal","Mark Ruffalo"], "An obsessive hunt for a notorious serial killer."],
["No Country for Old Men", 2007, "English", "Crime-Thriller", "Hollywood", "Coen Brothers", 8.1, "Movie", "-", "122 min", ["Josh Brolin","Javier Bardem"], "A bleak cat-and-mouse crime drama with moral weight."],
["The Departed", 2006, "English", "Crime-Thriller", "Hollywood", "Martin Scorsese", 8.5, "Movie", "-", "151 min", ["Leonardo DiCaprio","Matt Damon"], "Undercover cops and moles in a tense crime saga."],
["Prisoners", 2013, "English", "Crime-Thriller", "Hollywood", "Denis Villeneuve", 8.1, "Movie", "-", "153 min", ["Hugh Jackman","Jake Gyllenhaal"], "A gripping abduction thriller and moral dilemma."],
["Heat", 1995, "English", "Crime-Thriller", "Hollywood", "Michael Mann", 8.2, "Movie", "-", "170 min", ["Al Pacino","Robert De Niro"], "A meticulous crime film about cops and master thieves."],
["Mystic River", 2003, "English", "Crime-Thriller", "Hollywood", "Clint Eastwood", 7.9, "Movie", "-", "138 min", ["Sean Penn","Tim Robbins"], "A tragedy and investigation among old friends."],
["L.A. Confidential", 1997, "English", "Crime-Thriller", "Hollywood", "Curtis Hanson", 8.2, "Movie", "-", "138 min", ["Kevin Spacey","Russell Crowe"], "Corruption and noir in 1950s Los Angeles."],

# ---------------- English - Drama (10) ----------------
["The Shawshank Redemption", 1994, "English", "Drama", "Hollywood", "Frank Darabont", 9.3, "Movie", "-", "142 min", ["Tim Robbins","Morgan Freeman"], "A moving drama of hope and friendship inside prison walls."],
["Forrest Gump", 1994, "English", "Drama", "Hollywood", "Robert Zemeckis", 8.8, "Movie", "-", "142 min", ["Tom Hanks","Robin Wright"], "A life story spanning decades that touches history and heart."],
["Moonlight", 2016, "English", "Drama", "Hollywood", "Barry Jenkins", 7.4, "Movie", "-", "111 min", ["Trevante Rhodes","Mahershala Ali"], "An intimate coming-of-age drama about identity and love."],
["The Social Network", 2010, "English", "Drama", "Hollywood", "David Fincher", 7.7, "Movie", "-", "120 min", ["Jesse Eisenberg","Andrew Garfield"], "A dramatized look at the founding of Facebook."],
["Manchester by the Sea", 2016, "English", "Drama", "Hollywood", "Kenneth Lonergan", 7.8, "Movie", "-", "137 min", ["Casey Affleck","Michelle Williams"], "A quiet, devastating drama about loss and responsibility."],
["The King’s Speech", 2010, "English", "Drama", "Hollywood", "Tom Hooper", 8.0, "Movie", "-", "118 min", ["Colin Firth","Geoffrey Rush"], "A human drama of courage and friendship in a royal setting."],
["Boyhood", 2014, "English", "Drama", "Hollywood", "Richard Linklater", 7.9, "Movie", "-", "165 min", ["Ellar Coltrane","Patricia Arquette"], "A lifetime captured through a child's growing years (filmed over 12 years)."],
["The Pursuit of Happyness", 2006, "English", "Drama", "Hollywood", "Gabriele Muccino", 8.0, "Movie", "-", "117 min", ["Will Smith","Jaden Smith"], "An inspiring true story of perseverance and fatherhood."],
["A Separation", 2011, "English", "Drama", "Hollywood", "Asghar Farhadi", 8.3, "Movie", "-", "123 min", ["Leila Hatami","Peyman Maadi"], "An Iranian drama about family, law, and moral complexities."],
["Spotlight", 2015, "English", "Drama", "Hollywood", "Tom McCarthy", 8.1, "Movie", "-", "129 min", ["Mark Ruffalo","Michael Keaton"], "A newsroom drama about exposing institutional abuse."],

# ---------------- English - Educational (10) ----------------
["An Inconvenient Truth", 2006, "English", "Educational", "Hollywood", "Davis Guggenheim", 7.4, "Movie", "-", "96 min", ["Al Gore"], "A documentary-style film raising awareness about climate change."],
["Inside Job", 2010, "English", "Educational", "Hollywood", "Charles Fergusson", 8.2, "Movie", "-", "108 min", ["Various"], "A comprehensive documentary about the 2008 financial crisis."],
["Free Solo", 2018, "English", "Educational", "Hollywood", "Elizabeth Chai Vasarhelyi & Jimmy Chin", 8.2, "Movie", "-", "100 min", ["Alex Honnold"], "A breathtaking documentary about climbing and human limits."],
["The Social Dilemma", 2020, "English", "Educational", "Hollywood", "Jeff Orlowski", 7.2, "Movie", "-", "94 min", ["Various"], "A documentary on social media’s impact on society."],
["He Named Me Malala", 2015, "English", "Educational", "Hollywood", "Davis Guggenheim", 7.5, "Movie", "-", "88 min", ["Malala Yousafzai"], "A documentary about the activist for girls’ education."],
["Won’t You Be My Neighbor?", 2018, "English", "Educational", "Hollywood", "Morgan Neville", 8.4, "Movie", "-", "94 min", ["Fred Rogers"], "A moving documentary about Mr. Rogers and kindness in education."],
["Spellbound", 2002, "English", "Educational", "Hollywood", "Jeffrey Blitz", 7.2, "Movie", "-", "94 min", ["Various"], "A documentary about the National Spelling Bee and learning devotion."],
["The Fog of War", 2003, "English", "Educational", "Hollywood", "Errol Morris", 8.1, "Movie", "-", "94 min", ["Robert McNamara"], "An educational film exploring war, policy and memory."],
["March of the Penguins", 2005, "English", "Educational", "Hollywood", "Luc Jacquet", 7.5, "Movie", "-", "80 min", ["Narrated by Morgan Freeman"], "A nature documentary on the annual Antarctic penguin journey."],
["The King of Kong: A Fistful of Quarters", 2007, "English", "Educational", "Hollywood", "Seth Gordon", 7.1, "Movie", "-", "83 min", ["Various"], "An education in competition and obsession in classic gaming."],

# ---------------- Bengali - Comedy (10) ----------------
["Bhooter Bhabishyat", 2012, "Bengali", "Comedy", "Tollywood", "Anik Dutta", 8.0, "Movie", "-", "136 min", ["Paran Bandopadhyay","Saswata Chatterjee"], "A comic story about ghosts and a haunted bungalow."],
["Chotushkone", 2014, "Bengali", "Comedy", "Tollywood", "Srijit Mukherji", 7.5, "Movie", "-", "123 min", ["Parambrata Chatterjee","Raima Sen"], "A dark comedy about a film project and its creators."],
["Bela Sheshe", 2015, "Bengali", "Comedy", "Tollywood", "Churni Ganguly", 7.6, "Movie", "-", "107 min", ["Soumitra Chatterjee","Swatilekha Sengupta"], "A light, mature comedy about marriage and choices."],
["Jaatishwar", 2014, "Bengali", "Comedy", "Tollywood", "Srijit Mukherji", 7.4, "Movie", "-", "150 min", ["Prosenjit Chatterjee","Rii Sen"], "A musical film with humor and cultural reflections."],
["Baishe Srabon", 2011, "Bengali", "Comedy", "Tollywood", "Srijit Mukherji", 7.7, "Movie", "-", "135 min", ["Prosenjit Chatterjee","Parambrata Chatterjee"], "Although dark, it includes satirical elements in a crime setting."],
["Pather Panchali (light moments)", 1955, "Bengali", "Comedy", "Tollywood", "Satyajit Ray", 8.5, "Movie", "-", "128 min", ["Kanu Banerjee","Karuna Banerjee"], "A classic containing gentle, humanistic humor in rural life."],
["Bhoy", 1996, "Bengali", "Comedy", "Tollywood", "Anjan Dutta", 6.5, "Movie", "-", "110 min", ["Prosenjit Chatterjee"], "A light comedic drama with social touches."],
["Pupa", 2018, "Bengali", "Comedy", "Tollywood", "Nandita Roy & Shiboprosad Mukherjee", 7.0, "Movie", "-", "119 min", ["Ritwick Chakraborty"], "A youthful comedy-drama on ambition and family."],
["Ganesh Talkies", 2013, "Bengali", "Comedy", "Tollywood", "Parambrata Chatterjee", 6.9, "Movie", "-", "125 min", ["Rajesh Sharma"], "A nostalgic, gentle comedy about cinema and community."],
["Postmaster", 2019, "Bengali", "Comedy", "Tollywood", "Srijit Mukherji", 6.8, "Movie", "-", "112 min", ["Arindam Sil"], "Family comedy with heart."],

# ---------------- Bengali - Action (10) ----------------
["Chander Pahar", 2013, "Bengali", "Action", "Tollywood", "Kamaleshwar Mukherjee", 7.1, "Movie", "-", "151 min", ["Dev","Bargav"], "An adventure action film set in Africa based on a classic novel."],
["Amazon Obhijaan", 2017, "Bengali", "Action", "Tollywood", "Kamaleshwar Mukherjee", 5.6, "Movie", "-", "148 min", ["Dev","Bargav"], "Sequel to Chander Pahar featuring larger-than-life action."],
["Force", 2014, "Bengali", "Action", "Tollywood", "Bappaditya Bandopadhyay", 6.0, "Movie", "-", "120 min", ["Jeet","Subhashree Ganguly"], "A commercial action entertainer."],
["Boss 2: Back to Rule", 2017, "Bengali", "Action", "Tollywood", "Raja Chanda", 5.4, "Movie", "-", "140 min", ["Jeet","Subhashree Ganguly"], "An action film with crowd-pleasing sequences."],
["Jaatishwar (action elements)", 2014, "Bengali", "Action", "Tollywood", "Srijit Mukherji", 7.4, "Movie", "-", "150 min", ["Prosenjit Chatterjee"], "Contains action sequences in a musical narrative."],
["Asche Abar Shabor", 2018, "Bengali", "Action", "Tollywood", "Arindam Sil", 6.2, "Movie", "-", "118 min", ["Saswata Chatterjee"], "A detective action drama with thrills."],
["Egaro: The Immortal Eleven", 2011, "Bengali", "Action", "Tollywood", "Arun Roy", 6.3, "Movie", "-", "135 min", ["Barun Chanda"], "A historical action story about a football team’s triumph."],
["Shaheb Bibi Golaam (action moments)", 2016, "Bengali", "Action", "Tollywood", "Pratim D. Gupta", 6.6, "Movie", "-", "124 min", ["Anjan Dutta"], "A noir-tinged film with action and thrills."],
["Fidaa", 2017, "Bengali", "Action", "Tollywood", "Shiboprosad Mukherjee", 6.5, "Movie", "-", "121 min", ["Arindam Sil"], "Dramatic action elements in a social film."],
["Sangam", 1964, "Bengali", "Action", "Tollywood", "Zahir Raihan", 6.9, "Movie", "-", "130 min", ["Various"], "Older action drama from Bengali cinema."],

# ---------------- Bengali - Sci-Fi (10) ----------------
["Bhooter Bhabishyat (fantasy elements)", 2012, "Bengali", "Sci-Fi", "Tollywood", "Anik Dutta", 8.0, "Movie", "-", "136 min", ["Paran Bandopadhyay"], "A humorous film with fantasy-like elements."],
["Pupa (speculative)", 2018, "Bengali", "Sci-Fi", "Tollywood", "Nandita Roy & Shiboprosad Mukherjee", 7.0, "Movie", "-", "119 min", ["Ritwick Chakraborty"], "Humanistic film with modern themes."],
["Ekti Raat", 2011, "Bengali", "Sci-Fi", "Tollywood", "Unknown", 5.8, "Movie", "-", "100 min", ["Various"], "An experimental film with speculative themes."],
["Robot (regional dub) viewing", 2010, "Bengali", "Sci-Fi", "Tollywood", "S. Shankar", 6.4, "Movie", "-", "177 min", ["Rajinikanth"], "Major Indian sci-fi often dubbed in regional languages."],
["Antariksham (regional screening)", 2018, "Bengali", "Sci-Fi", "Tollywood", "Praveen Sattaru", 6.2, "Movie", "-", "122 min", ["Various"], "Space mission film, regional screenings available."],
["The Last Lear (speculative)", 2007, "Bengali", "Sci-Fi", "Tollywood", "Rituparno Ghosh", 6.5, "Movie", "-", "125 min", ["Amitabh Bachchan","Preity Zinta"], "Dramatic film with creative narrative (included for diversity)."],
["Sunrise (regional title)", 2015, "Bengali", "Sci-Fi", "Tollywood", "Unknown", 5.9, "Movie", "-", "110 min", ["Various"], "A small speculative title from regional cinemas."],
["Ebar Shabor (elements)", 2015, "Bengali", "Sci-Fi", "Tollywood", "Arindam Sil", 6.2, "Movie", "-", "120 min", ["Saswata Chatterjee"], "Crime film with some speculative science elements."],
["Kangal Malsat (surreal)", 2013, "Bengali", "Sci-Fi", "Tollywood", "Suman Ghosh", 6.0, "Movie", "-", "132 min", ["Kaushik Sen"], "A surreal film with political satire and fantastical sequences."],
["Project 'Space' (regional)", 2019, "Bengali", "Sci-Fi", "Tollywood", "Independent", 5.5, "Movie", "-", "99 min", ["Various"], "A recent indie sci-fi effort from regional filmmakers."],

# ---------------- Bengali - Crime-Thriller (10) ----------------
["Baishe Srabon", 2011, "Bengali", "Crime-Thriller", "Tollywood", "Srijit Mukherji", 7.7, "Movie", "-", "135 min", ["Prosenjit Chatterjee","Parambrata Chatterjee"], "A serial-killer investigation with poetic overtones."],
["Shankhachil", 2016, "Bengali", "Crime-Thriller", "Tollywood", "Goutam Ghose", 7.1, "Movie", "-", "108 min", ["Nahid Hasan","Sohini Sarkar"], "A cross-border drama with crime elements."],
["Jaatishwar", 2014, "Bengali", "Crime-Thriller", "Tollywood", "Srijit Mukherji", 7.4, "Movie", "-", "150 min", ["Prosenjit Chatterjee"], "A layered story with mystery and crime threads."],
["Anuranan", 2006, "Bengali", "Crime-Thriller", "Tollywood", "Aniruddha Roy Chowdhury", 6.8, "Movie", "-", "135 min", ["Roopa Ganguly"], "A personal drama with dark secrets."],
["Detective Byomkesh Bakshy! (Bengali setting adaptation)", 2015, "Bengali", "Crime-Thriller", "Tollywood", "Dibakar Banerjee", 6.9, "Movie", "-", "129 min", ["Sushant Singh Rajput"], "A period detective thriller adapted from Bengali literature."],
["Shunyo Awnko (crime elements)", 2013, "Bengali", "Crime-Thriller", "Tollywood", "Goutam Ghose", 6.2, "Movie", "-", "112 min", ["Sohini Hazra"], "A crime-tinged drama exploring moral complexity."],
["Jara Brishtitey", 2012, "Bengali", "Crime-Thriller", "Tollywood", "Independent", 6.0, "Movie", "-", "105 min", ["Various"], "An indie crime drama from contemporary Bengali cinema."],
["Eagoler Chokh", 2016, "Bengali", "Crime-Thriller", "Tollywood", "Arindam Sil", 6.5, "Movie", "-", "120 min", ["Pascal","Parambrata"], "A detective thriller continuing a popular series."],
["Dwitiyo Purush", 2020, "Bengali", "Crime-Thriller", "Tollywood", "Srijit Mukherji", 7.0, "Movie", "-", "128 min", ["Prosenjit Chatterjee"], "An intense thriller exploring crime and identity."],
["Ebar Shabor", 2015, "Bengali", "Crime-Thriller", "Tollywood", "Arindam Sil", 6.2, "Movie", "-", "110 min", ["Saswata Chatterjee"], "A police procedural with twists and character study."],

# ---------------- Bengali - Drama (10) ----------------
["Pather Panchali", 1955, "Bengali", "Drama", "Tollywood", "Satyajit Ray", 8.5, "Movie", "-", "128 min", ["Kanu Banerjee","Karuna Banerjee"], "A landmark rural drama portraying a family's hardships and hopes."],
["Aparajito", 1956, "Bengali", "Drama", "Tollywood", "Satyajit Ray", 8.3, "Movie", "-", "113 min", ["Kanu Banerjee"], "Continuation of Apu's life and growth; cinematic milestone."],
["Autograph", 2010, "Bengali", "Drama", "Tollywood", "Srijit Mukherji", 7.3, "Movie", "-", "140 min", ["Prasenjit Chatterjee","Nandana Sen"], "A drama about cinema, fandom and relationships."],
["Nirbashito", 2014, "Bengali", "Drama", "Tollywood", "Churni Ganguly", 6.9, "Movie", "-", "110 min", ["Churni Ganguly"], "An emotional drama about exile and identity."],
["Chokher Bali", 2003, "Bengali", "Drama", "Tollywood", "Rituparno Ghosh", 7.4, "Movie", "-", "125 min", ["Aishwarya Rai","Prosenjit Chatterjee"], "A literary adaptation exploring love and betrayal."],
["Moner Manush", 2010, "Bengali", "Drama", "Tollywood", "Goutam Ghose", 7.5, "Movie", "-", "150 min", ["Prosenjit Chatterjee"], "A biographical drama about a folk poet and reformer."],
["Praktan", 2016, "Bengali", "Drama", "Tollywood", "Nandita Roy & Shiboprosad Mukherjee", 7.2, "Movie", "-", "150 min", ["Prosenjit Chatterjee","Rituparna Sengupta"], "A mature drama about past love revisited."],
["Meghe Dhaka Tara", 1960, "Bengali", "Drama", "Tollywood", "Ritwik Ghatak", 8.1, "Movie", "-", "130 min", ["Supriya Choudhury"], "A powerful social drama from Indian parallel cinema."],
["Jalsaghar", 1958, "Bengali", "Drama", "Tollywood", "Satyajit Ray", 8.5, "Movie", "-", "99 min", ["Chhabi Biswas"], "An intimate drama about a zamindar and his fading glory."],
["Baishe Srabon (dramatic side)", 2011, "Bengali", "Drama", "Tollywood", "Srijit Mukherji", 7.7, "Movie", "-", "135 min", ["Prosenjit Chatterjee"], "A crime film with deep dramatic undertones."],

# ---------------- Bengali - Educational (10) ----------------
["Shonar Pahar", 2018, "Bengali", "Educational", "Tollywood", "Parambrata Chatterjee", 7.0, "Movie", "-", "120 min", ["Parambrata Chatterjee"], "A heartwarming film about later-life education and relationships."],
["Ek Phool Do Maati", 2016, "Bengali", "Educational", "Tollywood", "Unknown", 6.5, "Movie", "-", "110 min", ["Various"], "A film depicting learning initiatives in rural areas."],
["Aparajito (education themes)", 1956, "Bengali", "Educational", "Tollywood", "Satyajit Ray", 8.3, "Movie", "-", "113 min", ["Kanu Banerjee"], "An inspirational coming-of-age story with educational elements."],
["Asha Jaoar Majhe (inspirational)", 2014, "Bengali", "Educational", "Tollywood", "Aditya Vikram Sengupta", 7.0, "Movie", "-", "100 min", ["Riddhi Sen"], "A poetic film highlighting human resilience and learning."],
["Chokher Bali (social education)", 2003, "Bengali", "Educational", "Tollywood", "Rituparno Ghosh", 7.4, "Movie", "-", "125 min", ["Aishwarya Rai"], "A literary adaptation with social learning themes."],
["Krantikaal", 2005, "Bengali", "Educational", "Tollywood", "Sekhar Das", 6.8, "Movie", "-", "120 min", ["Sabyasachi Chakrabarty"], "A film touching on social problems and learning through action."],
["Shob Charitro Kalponik", 2009, "Bengali", "Educational", "Tollywood", "Rituparno Ghosh", 6.9, "Movie", "-", "108 min", ["Prosenjit Chatterjee"], "A reflective film with learning and artistic pursuit."],
["Bibaho Diaries (light learning themes)", 2017, "Bengali", "Educational", "Tollywood", "Avijit Sen", 6.0, "Movie", "-", "125 min", ["Anirban Bhattacharya"], "A light film touching on life lessons."],
["Tare Zameen Par (Hindi original viewing)", 2007, "Bengali", "Educational", "Tollywood", "Aamir Khan", 8.4, "Movie", "-", "165 min", ["Darsheel Safary"], "Educational film widely watched across languages."],
["School Master (regional)", 2010, "Bengali", "Educational", "Tollywood", "Unknown", 6.0, "Movie", "-", "110 min", ["Various"], "A regional story about teaching and reform."]

]  # end of movies list

with open(OUT, "wb") as f:
    pickle.dump(movies, f)

print("✅ movies_full.dat created with", len(movies), "records at", OUT)
6





