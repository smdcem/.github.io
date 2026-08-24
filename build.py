#!/usr/bin/env python3
"""
Generates index.html, cv.html and projects/*.html from the data below.
Run: python3 build.py
Re-run any time you edit the data structures — it overwrites the HTML.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("Home", "index.html"),
    ("CV", "cv.html"),
    ("Kleroterion", "projects/kleroterion.html"),
    ("\u6c34\u6258\u90a6 Hydrotopia", "projects/hydrotopia.html"),
    ("Celestial Palpitations (Performance)", "projects/celestial-palpitations-performance.html"),
    ("Celestial Palpitations (Installation)", "projects/celestial-palpitations-installation.html"),
    ("Oneiric Kitchen", "projects/oneiric-kitchen.html"),
    ("mmm", "projects/mmm.html"),
    ("PARADISE", "projects/paradise.html"),
    ("\u3061\u3088 Chiyo", "projects/chiyo.html"),
    ("At Altitude", "projects/at-altitude.html"),
    ("Entanglement of Consciousness", "projects/entanglement-of-consciousness.html"),
    ("Austin", "projects/austin.html"),
]

PROJECTS = [
    dict(
        slug="kleroterion",
        title="Kleroterion",
        subtitle="(Work in progress)",
        jp_title="",
        year="2026",
        medium="Super 8 transferred to HD, colour, sound",
        duration="09:26",
        tags=["Video", "Installation"],
        desc=[
            "Observed through the workers and machines of the pachinko parlour Rakuen (\u201cParadise\u201d), Kleroterion examines the intersection between work and leisure, questioning what constitutes democracy today.",
        ],
        original_text=[],
        media_captions=[
            "Perfect Cube, 2026 (Photo: Jacky Yaan-Yuan Kuo)",
            "Short Circuit exhibition view at Pachinko Oslo (Photo: Jacky Yaan-Yuan Kuo)",
        ],
        media_count=4,
        credits=[
            ("Many thanks", "PARADISE AIR, Hamatomo Corporation, Rakuen Matsudo Branch, Tadafumi Kajitani \u68b6\u8c37\u5fe0\u53f2, Sun Park, Morgan Quaintance, Stephanie Mourey, Tom Lowe, Lux, R3store Studios"),
        ],
        history_title="Exhibition and Screening History",
        history=[
            ("2026", [
                ("Short Circuit, Pachinko Oslo, NO", "https://www.pachinko.no/future"),
                ("PARADISE: films by Chiemi Shimada, Kunstnernes Hus, Oslo, NO", "https://kunstnerneshus.no/en/program/cinema/paradise"),
            ]),
        ],
    ),
    dict(
        slug="hydrotopia",
        title="\u6c34\u6258\u90a6 Hydrotopia",
        subtitle="",
        jp_title="",
        year="2026",
        medium="Film and Live Performance",
        duration="50:00",
        tags=["Performance", "Video"],
        desc=[
            "In extreme cold, the human body can turn against itself through paradoxical undressing: failing nerves mistake freezing for heat, compelling the dying to shed their last protection. In \u6c34\u6258\u90a6 (Hydrotopia), hydrophones frozen into a block of ice capture the material disintegration of their frozen body as a projected film gradually emerges into clarity.",
            "The film follows artist Jamie Man suspended by hooks pierced through flesh in a British winter landscape, practising rituals rooted in Shiva-dedicated traditions that explore a state of perpetual non-being. As the ice surrenders its form and the image sharpens into focus, transformation itself becomes the subject: matter abandoning one state for another, the body held suspended between dissolution and emergence.",
            "\u2014 Tim Leyendekker, WORM",
        ],
        original_text=[],
        media_captions=[
            "Performance view at WORM, the International Film Festival Rotterdam (Photo credit: Matilde Gastaldo)",
        ],
        media_count=2,
        credits=[
            ("Flesh hook suspension", "Jamie Man"),
            ("Flesh hook suspension design and facilitation", "Tam Smith (@stateofblissuk)"),
            ("Film", "Chiemi Shimada"),
            ("Sound performance and sound design", "Jamie Man"),
            ("Producer", "Borre van Leeuwen (IFFR), Tim Leyendekker (WORM)"),
            ("Produced by", "WORM with the International Film Festival Rotterdam"),
            ("Special thanks", "Morgan Quaintance, Jim Farrant, Marijn Cinjee, and the volunteers who helped build the vibroacoustic floor"),
        ],
        history_title="Performance History",
        history=[
            ("2026", [("Art Directions: sound//vision, International Film Festival Rotterdam, NL", None)]),
        ],
    ),
    dict(
        slug="celestial-palpitations-performance",
        title="Celestial Palpitations",
        subtitle="(Performance)",
        jp_title="",
        year="2024\u201325",
        medium="80 medicine sachet collages in slide mounts, 2 carousel projectors, 1 digital projector, 2 contact mics and synthesisers, amps, gels, mirrors \u2014 dimensions variable",
        duration="20:00",
        tags=["Performance"],
        desc=[
            "Celestial Palpitations is a performance by artist-filmmaker Chiemi Shimada and composer and conductor Jamie Man, exploring the liminal state between being asleep and awake. It combines a slide projection work with the same title and improvised sounds that emphasise the projector\u2019s mechanism. These rhythms evoke the sensation of heart palpitations, one of the side effects of the medicine Ritalin, the packets of which are being used for creating the slides.",
            "This work is inspired by two things: the everyday act of opening medicine packets by Shimada's brother, who suffers from narcolepsy, and the psychophysiological state accompanying this action.",
            "This performance is part of Shimada's ongoing research project exploring the phenomenon of sleep and sleep disorders.",
        ],
        original_text=[],
        media_captions=[
            "Performance at Attenborough Centre for the Creative Arts, 2025",
            "Performance at Cafe Oto, 2025 (photo credit: Olga Paczka)",
        ],
        media_count=4,
        credits=[],
        history_title="Performance History",
        history=[
            ("2025", [
                ("Attenborough Centre for the Creative Arts, Brighton, UK", None),
                ("Courtisane Festival, Ghent, BE", None),
                ("Cafe Oto, London, UK", None),
            ]),
            ("2024", [("Earthwork, Spanners, London, UK", None)]),
        ],
    ),
    dict(
        slug="celestial-palpitations-installation",
        title="Celestial Palpitations",
        subtitle="(Installation)",
        jp_title="\u5929\u4f53\u306e\u52d5\u60b8",
        year="2024",
        medium="80 medicine sachet collages in slide mounts \u2014 dimensions variable",
        duration="",
        tags=["Installation"],
        desc=[
            "Celestial Palpitations is inspired by the everyday ritual of opening sachets of methylphenidate (marketed as Ritalin and Concerta), a medication taken by the artist's brother to manage narcolepsy. The work draws from the liminal states he inhabits as the packets are opened and the medication begins to mediate the boundaries between sleep and wakefulness.",
            "Enlarged, illuminated, and torn impressions of the sachets immerse viewers in a threshold where consciousness and unconsciousness converge, revealing dreamlike, veiled landscapes. Printed on each packet is a small black star, a regulatory mark indicating that only one tablet remains, designed to help patients monitor their medication.",
            "In this work, the printed star becomes more than a functional symbol. It mediates the shifting terrain between sleep and wake while serving as an anchor that helps orient the medicine taker through these transitional states. Moving between reality and imagination, the star resists clear divisions, suggesting that the boundaries between the two are porous rather than fixed.",
            "This slide projection work is part of the artist's ongoing project on sleep that involves collaborative workshops, 'Oneiric Kitchen', with a well-being practitioner, Susie Cunningham.",
        ],
        original_text=[],
        media_captions=[],
        media_count=2,
        video_id="2BYJ576OAA4",
        credits=[],
        history_title="Exhibition History",
        history=[
            ("2024", [("Remains, Greatorex Street, London, UK", None)]),
        ],
    ),
    dict(
        slug="oneiric-kitchen",
        title="Oneiric Kitchen",
        subtitle="",
        jp_title="",
        year="2025",
        medium="16mm film transferred to HD, colour, sound",
        duration="11:17",
        tags=["Video", "Workshop"],
        desc=[
            "Oneiric Kitchen emerges from a collaboration between Susie Cunningham, a wellbeing practitioner, and Chiemi Shimada, an artist-filmmaker. Weaving together therapeutic cooking workshops and conversations on rest, the film reflects on the thresholds of sleep and sleeplessness. It forms part of an ongoing research enquiry into the phenomenon of sleep and the complexities of sleep disorders.",
        ],
        original_text=[],
        media_captions=[],
        media_count=4,
        credits=[
            ("Workshop facilitator", "Susie Cunningham"),
            ("Project partners", "Colette Griffin and Rebecca Beinart (Primary), Asako Fujioka (Documentary Dream Center), British Council"),
            ("Interpreter", "Asako Fujioka"),
            ("Sound recordists", "Tom Harris (Nottingham), Kanshi Iwasaki (Chiba)"),
            ("Participants \u2014 Nottingham", "Alaika, Chiara, Colette, Paul, Rita, Saima, Tom"),
            ("Participants \u2014 Chiba", "Pooh, Setsuko, Ta, Takashi, Vika, Wendy, Yukiko"),
            ("Thanks to", "Hiroko Takebe (British Council), omusubi\u4e0d\u52d5\u7523 omusubi estate, \u96a0\u5c45\u5c4b IN kyo-Ya, PARADISE AIR, \u7d14\u55ab\u8336 \u82e5\u677e Jun-Kissa Wakamatsu, my family, Morgan Quaintance"),
            ("Support", "British Council\u2019s Connections Through Culture grant programme"),
        ],
        history_title=None,
        history=[],
    ),
    dict(
        slug="mmm",
        title="mmm",
        subtitle="",
        jp_title="",
        year="2023",
        medium="HD, B&W and colour, sound",
        duration="07:06",
        tags=["Video"],
        desc=[
            "mmm traces an eclectic constellation of clouds across Japanese cinema from the 1920s to the present. Taking inspiration from the 35mm film materials of physicist and cloud expert Masanao Abe (1891\u20131966) and from scientist Tapio Schneider's speculation that climate change could one day produce a cloudless sky, the film treats formlessness as an essential actor in the history of cinema.",
        ],
        original_text=[],
        media_captions=[],
        media_count=3,
        credits=[
            ("Commissioned by", "Asian Film Archive"),
            ("Project consultants", "Daniel Hui and Matthew Barrington"),
        ],
        history_title="Screenings & Exhibitions",
        history=[
            ("2026", [("Selected 16, Barbican, London, UK", None)]),
            ("2025", [("Bangkok Experimental Film Festival, One Bangkok Forum, TH", None)]),
            ("2024", [
                ("AFIAS | SMIF Spain Moving Images Festival, Madrid, ES", None),
                ("Light Matter Film Festival, Kino Palais, Buenos Aires, AR", None),
                ("mmm, Mal Seh\u2019n Kino / SCHAUT! Exhibition Space, Nippon Connection, Frankfurt, DE", None),
                ("Minikino, Bali, ID", None),
                ("Monographs, San Art Gallery, Ho Chi Minh City, VN", None),
            ]),
            ("2023", [
                ("Arkipel \u2014 Jakarta International Documentary & Experimental Film Festival, ID", None),
                ("Forum Film Dokumenter Jogjakarta, ID", None),
                ("Dharamshala International Film Festival, McLeod Ganj, Himachal Pradesh, IN", None),
                ("Monographs 2023 showcase, Oldham Theatre, the National Archives of Singapore, SG", None),
            ]),
        ],
    ),
    dict(
        slug="paradise",
        title="PARADISE",
        subtitle="",
        jp_title="",
        year="2020",
        medium="35mm film photographs transferred to HD, colour, sound",
        duration="05:13",
        tags=["Video", "Installation"],
        desc=[
            "Inspired by the pachinko chapter from Roland Barthes\u2019 book The Empire of Signs, PARADISE explores the enmeshed relationship between labour, capitalism and play through kaleidoscopic visions of a pachinko parlour and polyphonic voices.",
        ],
        original_text=[],
        media_captions=[
            "Photo taken by Ayami Kawashima (for the site-specific video installation at PARADISE AIR's Open Studio)",
        ],
        media_count=3,
        credits=[
            ("Voices in French", "Cecile Aria, Luca Serventi"),
            ("Voices in Japanese", "Hitomi Ishii, Isao Kanemaki, Takashi Kuraya, Mei Miyauchi, Saki Shirokoji, Sari Murakami, Shogo Yamazaki"),
            ("With the generous support of", "Hamatomo Corporation, PARADISE AIR, and Rakuen Matsudo branch"),
        ],
        history_title="Exhibitions & Screenings",
        history=[
            ("2026", [("PARADISE: films by Chiemi Shimada, Kunstnernes Hus, Oslo, NO", "https://kunstnerneshus.no/en/program/cinema/paradise")]),
            ("2023", [("to move without friction, SET Woolwich, London, UK", None)]),
            ("2022", [("FAYD Digital Issue 2 LEXIS AXIS, online", None)]),
            ("2021", [("Minikino Film Week: Bali International Short Film Festival, ID", None)]),
            ("2020", [("PARADISE AIR, JP", None)]),
        ],
    ),
    dict(
        slug="chiyo",
        title="\u3061\u3088 Chiyo",
        subtitle="",
        jp_title="",
        year="2019",
        medium="16mm transferred to HD, colour, sound",
        duration="12:39",
        tags=["Video"],
        desc=[
            "Chiyo is a poetic exploration of the Japanese suburbs through the artist's reflection on the life of her grandmother. With a series of everyday moments in Yashio, from a summer fair to Buddhist rituals, the film meditates on family, intimacy and ageing.",
        ],
        original_text=[
            "\u65e5\u672c\u306e\u90ca\u5916\u306b\u4f4f\u3080\u7956\u6bcd\u306e\u3082\u3068\u3067\u3001\u77ed\u3044\u671f\u9593\u751f\u6d3b\u3092\u5171\u306b\u3057\u306a\u304c\u3089\u3001\u5f7c\u5973\u306e\u898b\u305f\u5922\u3001\u90ca\u5916\u3067\u306e\u751f\u6d3b\u3001\u590f\u796d\u308a\u3001\u304a\u76c6\u98a8\u666f\u3092\u901a\u3057\u3066\u3001\u4f5c\u8005\u304c\u63cf\u304f\u7956\u6bcd\u50cf\u309216\u30df\u30ea\u30d5\u30a3\u30eb\u30e0\u3067\u63cf\u304f\u3002\u5bb6\u65cf\u3001\u8001\u9f62\u3001\u89aa\u5bc6\u3055\u3001\u6642\u9593\u3001\u8a18\u61b6\u3092\u30c6\u30fc\u30de\u3068\u3057\u305f\u77ed\u7de8\u4f5c\u54c1\u3002",
        ],
        media_captions=[],
        media_count=3,
        credits=[
            ("Chiyo Kobayashi as", "Chiyo"),
            ("Sound mix by", "Ed Chappell"),
            ("Colour grading by", "Alex Grigoras"),
            ("Written, produced, directed, shot, sound recorded, and edited by", "Chiemi Shimada"),
        ],
        history_title="Exhibitions & Screenings",
        history=[
            ("2025", [
                ("Available Light, Courtisane Festival, Ghent, BE", None),
                ("Grandma's Grammar, Sapieha Palace, Vilnius, LT", None),
            ]),
            ("2024", [
                ("Open City Documentary Festival, London, UK", None),
                ("films. Domestic/Intimate, Feb gallery Tokyo, JP", None),
            ]),
            ("2023", [
                ("I was baptised in Fortnite, Antwerp Mansion, Manchester, UK", None),
                ("Otonari san Short Film Festival, SOOO dramatic!, Tokyo, JP", None),
            ]),
            ("2022", [
                ("NAE Open, New Art Exchange, Nottingham, UK", None),
                ("Girls in Film Festival \u2014 Baesianz presents: short films from Asian diaspora, House of Vans, London, UK", None),
                ("Babfilmfest, Matchstick Piehouse, London, UK", None),
                ("aCinema, Wisconsin, US (streaming)", "https://www.acinema.space/current-program"),
                ("Slow Forward #4, Indeks, Bandung, ID (streaming)", None),
            ]),
            ("2021", [
                ("hungry eyes festival, Giessen, DE", "https://hungryeyesfestival.de/das-festival"),
                ("Sixteen Journal, Paris, FR (streaming)", "https://www.sixteenjournal.com/films/chiyo-by-chiemi-shimada/"),
                ("Gunma Biennale for Young Artists, Museum of Modern Art, Gunma, JP", "http://mmag.pref.gunma.jp/exhibition/next.htm#biennale"),
                ("Moscow International Experimental Film Festival, RU", "https://mieff.com/program/crossroads_2021"),
                ("Typography Center for Contemporary Art, Krasnodar, RU", "http://typography-online.ru/2021/09/14/mieff-2/"),
                ("Wathann Film Festival, Yangon, MM", "https://wffcinema.com/category_movies/61ae12ed925ae66dfe0e3095/movies"),
                ("Videograms Film programme \u201cDesire-Love\u201d, Vilnius, LT", "https://skalvija.lt/filmas/filmu-programa-troskimas-meile/?show=215793"),
            ]),
            ("2020", [
                ("London Short Film Festival, UK", None),
                ("Aswan International Women Film Festival, EG", None),
                ("Courtisane Festival, Ghent, BE (canceled due to COVID)", None),
                ("Japanese Film Festival Nippon Connection, Frankfurt, DE", None),
                ("Minikino Film Week: Bali International Short Film Festival, ID", "https://minikino.org/filmweek/mfw6/2020iff/"),
                ("SeaShorts Film Festival, Ipoh, MY", "https://seashorts.org/special-programme-space-in-between/"),
                ("Vdrome (15\u201328 September, streaming)", "http://www.vdrome.org/"),
                ("dresdner schmalfilmtage, Dresden, DE", "https://schmalfilmtage.de/en/program/"),
                ("Linea d\u2019Ombra Festival, Salerno, IT", "https://www.lineadombrafestival.it/lineadoc-film-in-concorso/"),
                ("Visions in the Nunnery, London, UK", "https://bowarts.org/nunnery/visions-p3-benedict-drew-2020"),
            ]),
            ("2019", [
                ("Sheffield Doc/Fest, UK", None),
                ("San Sebasti\u00e1n International Film Festival, ES", None),
                ("Open City Documentary Film Festival, London, UK", None),
                ("Image Forum Festival, Tokyo, Nagoya & Kyoto, JP", None),
                ("Japanese Avant-garde and Experimental Film Festival, London, UK", None),
                ("Unforeseen International Experimental Film Festival, Belgrade, RS", None),
                ("Place M Film Festival, Tokyo, JP", None),
                ("Wilden: Mekas, Menken, Rindland, and Shimada, Wolf Kino, Berlin, DE", None),
                ("System of Care Season, Deptford Cinema, London, UK", None),
                ("Nagaoka Geijutsu Koujichu (\u9577\u5ca1\u82b8\u8853\u5de5\u4e8b\u4e2d), JP", None),
            ]),
        ],
    ),
    dict(
        slug="at-altitude",
        title="At Altitude",
        subtitle="",
        jp_title="",
        year="2019",
        medium="16mm transferred to HD, colour, sound",
        duration="02:44",
        tags=["Video"],
        desc=[
            "Made as a pilot film of Chiyo, At Altitude is a self-reflexive film of a filmmaker\u2019s brief visit to her grandmother in the Japanese suburbs. Not having seen her grandmother for several years, she uses a 16mm film camera as a mediation tool to reconnect with her grandmother. Interweaving the juxtaposition of inside and outside spaces, the film offers an intimate look at family life and ageing.",
        ],
        original_text=[],
        media_captions=[],
        media_count=2,
        credits=[],
        history_title="Screenings",
        history=[
            ("2025", [("Instant, Somers Gallery, London, UK", None)]),
            ("2019", [
                ("V Festival de Video nodoCCS, Barcelona, ES", None),
                ("Nippon Connection, Frankfurt, DE", None),
                ("Deptford Cinema, London, UK", None),
                ("Lux Moving Image, London, UK", None),
                ("ICA, London, UK", None),
            ]),
        ],
    ),
    dict(
        slug="entanglement-of-consciousness",
        title="Entanglement of Consciousness",
        subtitle="",
        jp_title="",
        year="2017\u20132019",
        medium="HD video, colour, sound",
        duration="03:56",
        tags=["Video"],
        desc=[
            "Entanglement of Consciousness reflects the filmmaker's anxiety as a person who lives abroad over the missile tests being carried out by the North Korean government in 2017. The film begins with a close-up shot of the eye of a sleeping Asian woman and a cat watching a cartoon, which is the first part of \u2018Duck and Cover\u2019 \u2014 the official 1951 United States civil defence film featuring Bert the Turtle, demonstrating the act of ducking and covering.",
            "A series of uncanny events occur: labour, sleep, and online conversations appear and disappear as windows on-screen, being shown alongside each other as if they were puzzle pieces coming together to create a whole picture. Entanglement of Consciousness playfully depicts the fear of the unknown regarding international politics, as well as the question: how long can fear persist?",
            "The recurring motif of cats refers to Schr\u00f6dinger's cat theory. We often don't realise that we are living in a state of war; we are always stuck in a constant state of anxiety between calm and impending danger. Knowing and not knowing. In many ways, our lack of clarity about this situation and the constant fear can make it seem like we won't ever know whether we're alive or dead until the box is opened and we know for certain.",
        ],
        original_text=[
            "2017\u5e74\u306b\u5317\u671d\u9bae\u304c\u884c\u306a\u3063\u305f\u30df\u30b5\u30a4\u30eb\u5b9f\u9a13\u306b\u5bfe\u3059\u308b\u3001\u5916\u56fd\u5c45\u4f4f\u8005\u3068\u3057\u3066\u306e\u500b\u4eba\u7684\u5371\u6a5f\u611f\u304b\u3089\u5236\u4f5c\u3055\u308c\u305f\u77ed\u7de8\u6620\u50cf\u3002\u7720\u3063\u3066\u3044\u308b\u30a2\u30b8\u30a2\u7cfb\u5973\u6027\u306e\u76ee\u306e\u63a5\u5199\u3068\u3001iPhone\u3067\u4e80\u306e\u30a2\u30cb\u30e1\u30fc\u30b7\u30e7\u30f3\u3092\u898b\u3066\u3044\u308b\u732b\u306e\u5834\u9762\u304b\u3089\u6620\u50cf\u306f\u59cb\u307e\u308b\u3002",
        ],
        media_captions=[],
        media_count=2,
        credits=[],
        history_title="Screenings",
        history=[
            ("2021", [
                ("Place M Film Festival, Tokyo, JP", None),
                ("Dream, Dreaming, Dreamt, Winnipeg, CA", "https://www.winnipegfilmgroup.com/event/cabin-fever-dream-dreaming-dreamt-experimental-films-for-teens/"),
            ]),
            ("2019", [
                ("European Media Art Festival: EMAF, Osnabr\u00fcck, DE", None),
                ("Deptford Cinema, London, UK", None),
                ("Lux Moving Image, London, UK", None),
                ("ICA, London, UK", None),
            ]),
            ("2018", [("BFI, London, UK", None)]),
        ],
    ),
    dict(
        slug="austin",
        title="Austin",
        subtitle="",
        jp_title="",
        year="2016",
        medium="Super 16mm transferred to HD, colour, sound",
        duration="02:13",
        tags=["Video"],
        desc=[
            "Austin is a journey through a young man\u2019s private landscape. He does not appear on screen but through his soundscapes, leading the audience through his home, exploring the space of his domesticity.",
            "The work is inspired by the artist's bereaved brother. She created a character based on her brother, replacing the scene from Japan to the UK, and created the work by looking at the traces of human presence through the still life, recalling the space of the house where he spent his last hours.",
        ],
        original_text=[
            "\u3042\u308b\u4eba\u7269\u306e\u79c1\u7684\u7a7a\u9593\u3068\u30b5\u30a6\u30f3\u30c9\u30b9\u30b1\u30fc\u30d7\u3092\u901a\u3057\u3066\u3001\u4eba\u9593\u306e\u5b58\u5728\u3092\u305d\u306e\u4e0d\u5728\u304b\u3089\u307f\u3064\u3081\u308b\u7791\u60f3\u7684\u4f5c\u54c1\u3002\u4eba\u7269\u306f\u6700\u5f8c\u307e\u3067\u753b\u9762\u306b\u59ff\u3092\u73fe\u3055\u305a\u3001\u4f4f\u5c45\u7a7a\u9593\u306b\u3042\u308b\u75d5\u8de1\u3060\u3051\u304c\u305d\u306e\u4eba\u7269\u306e\u5b58\u5728\u3092\u7269\u8a9e\u308b\u3002",
        ],
        media_captions=[],
        media_count=2,
        credits=[
            ("Director, producer, editor", "Chiemi Shimada"),
            ("Producers at Kingston University", "Richard Squires and Phillip Warnell"),
            ("Cinematographer", "Vron Harris"),
            ("Voice-over", "Lucas Jones"),
            ("Colourist, dubbing mixer", "Kwame Lestrade"),
            ("Assistant directors", "Leah Morris and Si\u00e2n Ayerst-Dyer"),
            ("Sound recordists", "Andrew Pickering-Copley and Si\u00e2n Ayerst-Dyer"),
            ("Commissioned by", "the Institute of Contemporary Arts and Kingston University for Channel 4"),
        ],
        history_title="Exhibitions & Screenings",
        history=[
            ("2024", [("Analogue Short Film Screening: BIPOC Folks Vol 2, not/nowhere, London, UK", None)]),
            ("2022", [("Film Free and Easy, Primary, Nottingham, UK", None)]),
            ("2020", [("Form No Form (streaming)", None)]),
            ("2019", [("Place M Film Festival, Tokyo, JP", None)]),
            ("2018", [("Playback Festival at ICA, London, UK", None)]),
            ("2016", [("Stop Play Record screenings at ICA, London, UK", None)]),
        ],
    ),
]

CV = dict(
    bio=[
        "Chiemi Shimada \u5cf6\u7530\u5343\u7d75\u7f8e is a London-based artist and filmmaker. Working across film, performance, installation, and workshops, she explores and interrogates memory, modernity, liminal states, and late-stage capitalism. Her work has been presented in galleries, museums and film festivals internationally, including International Film Festival Rotterdam, Open City Documentary Festival, Courtisane Festival, Arkipel, and the ICA London, Barbican, the National Archives of Singapore, Cineteca Nacional M\u00e9xico and Kunstnernes Hus.",
    ],
    place="Born and bred in Chiba, Japan \u2014 Lives and works in London, UK",
    contact=[
        ("Email", "mailto:chi00shi00@gmail.com"),
        ("Instagram", "https://www.instagram.com/smdcem/"),
        ("Vimeo", "http://vimeo.com/user15324621"),
    ],
    sections=[
        ("Exhibitions & Events", [
            ("2026", [
                ("A Machine as Complex as the World Itself, Korskirken, Bergen Assembly, NO (11/9)", "https://bergen-assembly.hoopla.no/event/811809799"),
                ("Loophole, Working From Home, London (22/8\u201312/9)", "https://wfh-project.com/"),
                ("Short Circuit, Pachinko Oslo, NO", "https://www.pachinko.no/future"),
                ("Collective Divination and Filmmaking Workshop w/ Sun Park, Queer East, ICA London, UK", "https://queereast.org.uk/"),
                ("\u6c34\u6258\u90a6 Hydrotopia w/ Jamie Man, International Film Festival Rotterdam, NL", None),
            ]),
            ("2025", [
                ("Celestial Palpitations w/ Jamie Man, Attenborough Centre for the Creative Arts, Brighton, UK", None),
                ("VHS/DTV, TACO!, London, UK", None),
                ("Celestial Palpitations w/ Jamie Man, Courtisane Festival, Ghent, BE", None),
                ("Celestial Palpitations w/ Jamie Man, Cafe Oto, London, UK", "https://www.cafeoto.co.uk/events/morgan-quaintance-available-light/"),
                ("Instant, Somers Gallery, London, UK", None),
            ]),
            ("2024", [
                ("Earthwork, Spanners, London, UK", None),
                ("Remains, Greatorex Street, London, UK", None),
                ("mmm, Mal Seh\u2019n Kino / SCHAUT! Exhibition Space, Nippon Connection, Frankfurt, DE", None),
                ("films. Domestic/Intimate, Feb gallery Tokyo, JP", None),
            ]),
            ("2023", [
                ("Z/I/N/E, WHITEHOUSE, Tokyo, JP", None),
                ("Monographs showcase, Oldham Theatre, the National Archives of Singapore, SG", None),
                ("to move without friction, SET Woolwich, London, UK", None),
                ("Sunscreen, Lux, London, UK", None),
                ("Between Different States, Bloc Projects, Sheffield, UK", None),
                ("I was baptised in Fortnite, Antwerp Mansion, Manchester, UK", None),
            ]),
            ("2022", [
                ("Blind Vision, Treptow Ateliers, Berlin, DE", "https://maikschierloh.de/art-events/blind-vision/"),
                ("FAYD DIGITAL Issue 002 lexis/axis, online", "https://fayddigital.com/Issue-002-Lexis-Axis"),
                ("NAE Open, New Art Exchange, Nottingham, UK", "http://www.nae.org.uk/exhibition/nae-open-2022/191"),
            ]),
            ("2021", [
                ("Gunma Biennale for Young Artists, Museum of Modern Art, Gunma, JP", "http://mmag.pref.gunma.jp/exhibition/next.htm#biennale"),
                ("sensitivity, Gallery rusu, Tokyo, JP", None),
            ]),
            ("2020", [
                ("Visions in the Nunnery, Nunnery Gallery, London, UK", "https://bowarts.org/nunnery/visions-p3-benedict-drew-2020"),
                ("PARADISE HOUR, PARADISE AIR, Chiba, JP", "https://www.paradiseair.info/en/news/2020/11/14/14222"),
                ("Non-museum for Contemporary Art, Gewandhaus Site, Dresden, DE", None),
            ]),
            ("2019", [("Video Art Forum, Maha Al Mansour, Dammam, SAU", None)]),
            ("2018", [("Campus Genius Award Exhibition, National Museum of Emerging Science and Innovation, Tokyo, JP", None)]),
            ("2016", [
                ("The Annual Juried Student Exhibition, Padnos Art Gallery, Grand Valley State University, MI, US", None),
                ("Kemi (duo show with Keziah Philipps), Padnos Art Gallery, Grand Valley State University, MI, US", None),
            ]),
        ]),
        ("Screenings", [
            ("2026", [
                ("Selected 16, CAST, Heston, Cornwall (date TBC)", None),
                ("Selected 16, Fabrica Gallery, Brighton (1/10)", None),
                ("Selected 16, Towner Eastbourne (26/9)", None),
                ("Selected 16, Offline, Glasgow (18/9)", None),
                ("Selected 16, G39, Cardiff (12/9)", None),
                ("Selected 16, Watershed with Spikes Island, Bristol (3/9)", None),
                ("Selected 16, Broadway with Nottingham Contemporary (2/9)", None),
                ("Monographs, 282 Workshop, Hanoi & N\u00e9m Space, Ho Chi Minh City, VN", None),
                ("Selected 16, Barbican, London, UK", "https://www.barbican.org.uk/whats-on/2026/event/experiments-in-film-selected-16"),
                ("PARADISE: films by Chiemi Shimada, Kunstnernes Hus, Oslo, NO", "https://kunstnerneshus.no/en/program/cinema/paradise"),
            ]),
            ("2025", [
                ("Cartographies of the Dark, K\u00f6X e.V., D\u00fcsseldorf, DE", None),
                ("Yamagata Documentary Dojo, Senshu University, Tokyo, JP", None),
                ("Open City Documentary Festival, Barbican, London, UK", "https://opencitylondon.com/events/combined-programme-available-light/"),
                ("Courtisane Festival, Ghent, BE", None),
                ("Grandma's Grammar, Sapieha Palace, Vilnius, LT", None),
                ("Bangkok Experimental Film Festival, One Bangkok Forum, TH", None),
            ]),
            ("2024", [
                ("Analogue Short Film Screening: BIPOC Folks Vol 2, not/nowhere, London, UK", "https://www.not-nowhere.org/on/analogue-short-film-screening-bipoc-folks-vol-2"),
                ("AFIAS | SMIF Spain Moving Images Festival, Madrid, ES", None),
                ("Light Matter Film Festival, Kino Palais, Buenos Aires, AR", "https://www.lightmatterfilmfestival.com/copy-of-program-4-1"),
                ("Oneiric Kitchen (WIP), Broadway Cinema, Nottingham, UK", None),
                ("Open City Documentary Festival, London, UK", None),
                ("Monographs, San Art Gallery, Ho Chi Minh City, VN", None),
                ("Birkbeck Institute for the Moving Image, London, UK", None),
                ("AV Tales, London, UK", None),
                ("Minikino, Bali, ID", None),
            ]),
            ("2023", [
                ("Forum Film Dokumenter Jogjakarta, ID", None),
                ("Dharamshala International Film Festival, McLeod Ganj, Himachal Pradesh, IN", None),
                ("Arkipel \u2014 Jakarta International Documentary & Experimental Film Festival, ID", None),
                ("Chichester International Film Festival, UK", None),
                ("Cinema Rediscovered, Watershed, Bristol, UK", None),
                ("Cinema Ritrovato, Auditorium \u2013 DAMSLab, Bologna, IT", None),
                ("Essay Film Festival, ICA, London, UK", None),
                ("Otonari san Short Film Festival, SOOO dramatic!, Tokyo, JP", "https://otonarisan.peatix.com/?fbclid=IwAR1TkG9Bb4dDhdPk7-cpyo-Xe5R33VONcHqYl4LyAyeh44SWCRNu0z6WmEQ"),
            ]),
            ("2022", [
                ("Film Free and Easy, Primary, Nottingham, UK", None),
                ("Centro de Cine Costa Rica, San Jos\u00e9, CR", None),
                ("Cineteca Nacional M\u00e9xico, Mexico City, MX", None),
                ("Babfilmfest, Matchstick Piehouse, London, UK", None),
                ("Nippon Connection, Frankfurt, DE", None),
                ("Girls in Film Festival \u2014 Baesianz presents: short films from Asian diaspora, House of Vans, London, UK", "https://www.eventbrite.co.uk/e/girls-in-film-festival-giff-sunday-tickets-326190443397"),
                ("aCinema, WI, US (streaming)", "https://www.acinema.space/archive/kirisame"),
                ("Brunswick Underground Film Festival, AU", None),
                ("Slow Forward #4, Indeks, Bandung, ID (streaming)", None),
            ]),
            ("2021", [
                ("Videograms Film programme \u201cDesire-Love\u201d, Skalvijos kino centras, Vilnius, LT", "https://skalvija.lt/filmas/filmu-programa-troskimas-meile/?show=215793"),
                ("Wathann Film Festival, Yangon, MM", "https://wffcinema.com/category_movies/61ae12ed925ae66dfe0e3095/movies"),
                ("Typography Center for Contemporary Art, Krasnodar, RU", "http://typography-online.ru/2021/09/14/mieff-2/"),
                ("Garage Screen, Moscow, RU", "https://garagemca.org/en/event/special-screening-of-the-6th-moscow-international-experimental-film-festival-mieff-and-image-forum"),
                ("Minikino Film Week: Bali International Short Film Festival, ID", None),
                ("Moscow International Experimental Film Festival, RU", "https://mieff.com/program/crossroads_2021"),
                ("Sixteen Journal, Paris, FR (streaming)", "https://www.sixteenjournal.com/films/chiyo-by-chiemi-shimada/"),
                ("Dream, Dreaming, Dreamt, Winnipeg, CA (streaming)", "https://www.winnipegfilmgroup.com/event/cabin-fever-dream-dreaming-dreamt-experimental-films-for-teens/"),
                ("Place M Film Festival, Tokyo, JP", "https://www.placemfilmfestival.tokyo/place-m-shorts"),
                ("hungry eyes festival, Giessen, DE", "https://hungryeyesfestival.de/das-festival"),
            ]),
            ("2020", [
                ("Linea d\u2019Ombra Festival, Salerno, IT", "https://www.lineadombrafestival.it/lineadoc-film-in-concorso/"),
                ("dresdner schmalfilmtage, Dresden, DE", "https://schmalfilmtage.de/en/program/"),
                ("Vdrome (streaming)", "http://www.vdrome.org/chiemi-shimada/"),
                ("SeaShorts Film Festival, MY", "https://seashorts.org/special-programme-space-in-between/"),
                ("Minikino Film Week: Bali International Short Film Festival, ID", "https://minikino.org/filmweek/mfw6/2020iff/"),
                ("Japanese Film Festival Nippon Connection, Frankfurt, DE", None),
                ("Form No Form (streaming)", "https://www.formnoform.com/"),
                ("Aswan International Women Film Festival, EG", None),
                ("London Short Film Festival, UK", "https://shortfilms.org.uk/lsff2020/events/2020-01-14-documentary-the-measure-of-a-moment"),
            ]),
            ("2019", [
                ("Place M Film Festival, Tokyo, JP", "https://film.placem.com/events/PlaceM_FilmFestival_2019.pdf"),
                ("V Festival de Video nodoCCS, Barcelona, ES", "https://mailchi.mp/e4a33b56c5ea/v_festival_video_nodoccs"),
                ("Unforeseen International Experimental Film Festival, Belgrade, RS", None),
                ("Nagaoka Geijutsu Koujichu (\u9577\u5ca1\u82b8\u8853\u5de5\u4e8b\u4e2d), Niigata, JP", None),
                ("System of Care Season at Deptford Cinema, London, UK", "http://deptfordcinema.org/new-events/americastollwhiteside2018"),
                ("San Sebasti\u00e1n International Film Festival, ES", "https://www.sansebastianfestival.com/2019/sections_and_films/nest_film_students/8/in"),
                ("Japanese Avant-garde and Experimental Film Festival, London, UK", "https://www.closeupfilmcentre.com/film_programmes/2019/jaeff-nation"),
                ("Image Forum Festival, Tokyo, Nagoya & Kyoto, JP", "http://www.imageforumfestival.com/bosyu2019/en.html"),
                ("Open City Documentary Festival, London, UK", "https://opencitylondon.com/events/shorts-i-have-seen-nothing-i-have-seen-all/"),
                ("Wilden: Mekas, Menken, Rindland, and Shimada at Wolf Kino, Berlin, DE", None),
                ("Sheffield Doc/Fest, UK", None),
                ("Japanese Film Festival Nippon Connection, Frankfurt, DE", None),
                ("European Media Art Festival: EMAF, Osnabr\u00fcck, DE", None),
            ]),
            ("2018", [("Playback Festival at ICA, London, UK", None)]),
            ("2017", [
                ("Up-and-coming International Film Festival Hannover, DE", None),
                ("Aesthetica Short Film Festival, York, UK", None),
                ("REC Film Festival, Berlin, DE", None),
            ]),
            ("2016", [
                ("Stop Play Record programme screening at ICA, London, UK", None),
                ("Chiaroscuro International Film Series at Urban Institute for Contemporary Arts, MI, US", None),
            ]),
        ]),
        ("Awards, Commissions, Residencies", [
            ("2024", [("Developing your Creative Practice, Arts Council England, UK", None)]),
            ("2023", [("Connections Through Culture Grant, British Council, UK", None)]),
            ("2022", [
                ("Monographs Film Commission, Asian Film Archive, SG", None),
                ("Primary Residency Prize, NAE Open 2022, Nottingham, UK", None),
            ]),
            ("2021", [("Yamagata Documentary Dojo, JP (online residency)", None)]),
            ("2020", [
                ("Matsudo \u201cQOL\u201d Residency Award, PARADISE AIR, Chiba, JP", None),
                ("Lokalen Foundation Residency, Lichtenvoorde, NL", None),
            ]),
            ("2019", [("Best UK Short Film Award Nominee, Open City Documentary Festival, London, UK", None)]),
            ("2018", [("Excellence Award in Art Category, Student Campus Genius Contest, Tokyo, JP", None)]),
            ("2015", [("Stop Play Record commission, ICA & Kingston University in partnership with Arts Council England, London, UK", None)]),
        ]),
        ("Education", [
            ("2022\u201324", [("School of the Damned", None)]),
            ("2022\u201323", [("LUX Critical Forum, LUX, London, UK", None)]),
            ("2017\u201319", [("MA Experimental Film (Distinction), Kingston School of Art, London, UK", None)]),
            ("2015\u201316", [("Exchange Study, Grand Valley State University, MI, US", None)]),
            ("2013\u201317", [("BA (Hons) Filmmaking (First-Class), Kingston School of Art, London, UK", None)]),
        ]),
        ("Apprenticeships", [
            ("2019", [
                ("Post-production assistant for Alia Syed", None),
                ("Assistant for Ben Rivers", None),
            ]),
        ]),
        ("Talks", [
            ("2020", [("London Short Film Festival Industry Panel: Articulating Diaspora, Rich Mix, London, UK", None)]),
            ("2019", [
                ("Filmmakers\u2019 Workshop at MetFilm School, Japanese Avant-garde and Experimental Film Festival, London, UK", None),
                ("Artist Talk at Kingston University, London, UK", None),
            ]),
        ]),
    ],
    interviews=[
        ("Interview about the making of \u201cChiyo\u201d, introduced by Peter Taylor, on Vdrome", "https://www.vdrome.org/chiemi-shimada"),
        ("\u201cChiyo\u201d review by Phil Coldiron", "https://philcoldiron.substack.com/p/chiyo?s=r"),
        ("Interview on Asian Movie Pulse", "https://asianmoviepulse.com/2019/10/interview-with-chiemi-shimada-i-think-the-borders-between-cinema-and-video-art-are-getting-blurred/"),
        ("\u201cChiyo\u201d review on Asian Movie Pulse", "https://asianmoviepulse.com/2020/03/short-film-review-chiyo-2019-by-chiemi-shimada/"),
        ("Japanese experimental documentary now (brief mention of \u201cChiyo\u201d), Sight & Sound / BFI", "https://www.bfi.org.uk/news-opinion/sight-sound-magazine/features/japanese-experimental-documentary-now-sheffield-docfest-2019"),
        ("Aspiring filmmakers at Kingston University given chance to step into the spotlight through Channel 4 programme Random Acts", "https://www.kingston.ac.uk/news/article/1805/08-mar-2017-aspiring-filmmakers-at-kingston-university-given-chance-to-step-into-the-spotlight-through-channel-4/"),
    ],
)


CV_JA = dict(
    sections=[
        ("展示 & イベント", [
            ("2026年", [
                ("A Machine as Complex as the World Itself, Korskirken, Bergen Assembly, NO (9/11)", "https://bergen-assembly.hoopla.no/event/811809799"),
                ("Loophole、Working From Home、ロンドン (8/22-9/12)", "https://wfh-project.com/"),
                ("Short Circuit、Pachinko Oslo、オスロ", "https://www.pachinko.no/future"),
                ("Collective Divination and Filmmaking Workshop (Sun Parkとの協働)、Queer East、ICA、ロンドン", "https://queereast.org.uk/"),
                ("水托邦 Hydrotopia (Jamie Manとの協働)、ロッテルダム国際映画祭", None),
            ]),
            ("2025年", [
                ("Celestial Palpitations (Jamie Manとの協働)、Attenborough Centre for the Creative Arts、ブライトン", None),
                ("VHS/DTV、TACO!、ロンドン", None),
                ("Celestial Palpitations (Jamie Manとの協働)、Courtisane Festival、ゲント", None),
                ("Celestial Palpitations (Jamie Manとの協働)、Cafe Oto、ロンドン", "https://www.cafeoto.co.uk/events/morgan-quaintance-available-light/"),
                ("Instant、Somers Gallery、ロンドン", None),
            ]),
            ("2024年", [
                ("Earthwork、Spanners、ロンドン", None),
                ("Remains、Greatorex Street、ロンドン", None),
                ("mmm、Mal Seh\u2019n Kino / SCHAUT! Exhibition Space、ニッポンコネクション、フランクフルト", None),
                ("films.ドメスティック/インティメイト、Feb gallery Tokyo", None),
            ]),
            ("2023年", [
                ("Z/I/N/E, WHITEHOUSE、東京", None),
                ("Monographs、Oldham Theatre、the National Archives of\u3000Singapore、シンガポール", None),
                ("to move without friction、SET Woolwich、ロンドン", None),
                ("Sunscreen、Lux、ロンドン", None),
                ("Between Different States, Bloc Projects、シェフィールド", None),
                ("I was baptised in Fortnite、Antwerp Mansion、マンチェスター", None),
            ]),
            ("2022年", [
                ("Blind Vision、Treptow Ateliers、ベルリン", "https://maikschierloh.de/art-events/blind-vision/"),
                ("FAYD DIGITAL Issue 002 lexis/axis、オンライン", "https://fayddigital.com/Issue-002-Lexis-Axis"),
                ("NAE Open、New Art Exchange、ノッティンガム", "http://www.nae.org.uk/exhibition/nae-open-2022/191"),
            ]),
            ("2021年", [
                ("群馬青年ビエンナーレ、群馬県立近代美術館", "http://mmag.pref.gunma.jp/exhibition/next.htm#biennale"),
                ("sensitivity、rusu、東京", None),
            ]),
            ("2020年", [
                ("Visions in the Nunnery、Nunnery Gallery、ロンドン", "https://bowarts.org/nunnery/visions-p3-benedict-drew-2020"),
                ("PARADISE HOUR、PARADISE AIR、千葉", "https://www.paradiseair.info/en/news/2020/11/14/14222"),
                ("Non-museum for Contemporary Art、Gewandhaus Site, ドレスデン", None),
            ]),
            ("2019年", [("Video Art Forum、Maha Al Mansour、ダンマーム", None)]),
            ("2018年", [("CG-ARTS協会 第23回学生CGコンテスト受賞作品展、日本科学未来館、東京", None)]),
            ("2016年", [
                ("The Annual Juried Student Exhibition、Padnos Art Gallery、グランドバレー州立大学、ミシガン", None),
                ("Kemi、Padnos Art Gallery、グランドバレー州立大学、ミシガン\uff08Keziah Philippsとの2人展\uff09", None),
            ]),
        ]),
        ("作品上映歴", [
            ("2026年", [
                ("Selected 16、CAST、Heston、コーンウォール (日程未定)", None),
                ("Selected 16、Fabrica Gallery、ブライトン (10/1)", None),
                ("Selected 16、Towner Eastbourne (9/26)", None),
                ("Selected 16、Offline、グラスゴー (9/18)", None),
                ("Selected 16、G39、カーディフ (9/12)", None),
                ("Selected 16、Watershed with Spikes Island、ブリストル (9/3)", None),
                ("Selected 16、Broadway with Nottingham Contemporary (9/2)", None),
                ("Monographs、282 Workshop、ハノイ & Ném Space、ホーチミン", None),
                ("Selected 16、Barbican、ロンドン", "https://www.barbican.org.uk/whats-on/2026/event/experiments-in-film-selected-16"),
                ("PARADISE: films by Chiemi Shimada、Kunstnernes Hus、オスロ", "https://kunstnerneshus.no/en/program/cinema/paradise"),
            ]),
            ("2025年", [
                ("Cartographies of the Dark | KöX e. V.、デュッセルドルフ", None),
                ("山形ドキュメンタリー道場、専修大学、東京", None),
                ("Open City Documentary Festival、Barbican、ロンドン", "https://opencitylondon.com/events/combined-programme-available-light/"),
                ("コーティザンフェスティバル、ゲント", None),
                ("Grandma's Grammar、Sapieha Palace、ビリニュス", None),
                ("Bangkok Experimental Film Festival、One Bangkok Forum、バンコク", None),
            ]),
            ("2024年", [
                ("Analogue Short Film Screening: BIPOC Folks Vol 2、not/nowhere、ロンドン", "https://www.not-nowhere.org/on/analogue-short-film-screening-bipoc-folks-vol-2"),
                ("AFIAS | SMIF Spain Moving Images Festival、マドリッド", None),
                ("Light Matter Film Festival、Kino Palais、ブエノスアイレス", "https://www.lightmatterfilmfestival.com/copy-of-program-4-1"),
                ("Oneiric Kitchen (WIP)、Broadway Cinema、ノッティンガム", None),
                ("Open City Documentary Festival、ロンドン", None),
                ("Monographs、San Art Gallery、ホーチミン", None),
                ("Birkbeck Institute for the Moving Image、ロンドン", None),
                ("AV Tales、ロンドン", None),
                ("Minikino、バリ", None),
            ]),
            ("2023年", [
                ("Forum Film Dokumenter Jogjakarta、ジョグジャカルタ", None),
                ("Dharamshala International Film Festival, ヒマチャルプラデシュ州ダラムサラ", None),
                ("Arkipel - Jakarta International Documentary & Experimental Film Festival、ジャカルタ", None),
                ("Chichester International Film Festival、チチェスター", None),
                ("Cinema Rediscovered、Watershed、ブリストル", None),
                ("Cinema Ritrovato、Auditorium – DAMSLab、ボローニャ", None),
                ("エッセイフィルムフェスティバル、ICA、ロンドン", None),
                ("おとなりさん短編映画祭、SOOO dramatic!、東京", "https://otonarisan.peatix.com/?fbclid=IwAR1TkG9Bb4dDhdPk7-cpyo-Xe5R33VONcHqYl4LyAyeh44SWCRNu0z6WmEQ"),
            ]),
            ("2022年", [
                ("Film Free and Easy、Primary、ノッティンガム", None),
                ("Centro de Cine Costa Rica、サンホセ", None),
                ("Cineteca Nacional México、メキシコシティ", None),
                ("Babfilmfest、Matchstick Piehouse、ロンドン", None),
                ("ニッポン・コネクション、フランクフルト", None),
                ("Girls in Film Festival Baesianz presents: short films from Asian diaspora、House of Vans、ロンドン", "https://www.eventbrite.co.uk/e/girls-in-film-festival-giff-sunday-tickets-326190443397"),
                ("aCinema、ウィスコンシン\uff08ストリーミング\uff09", "https://www.acinema.space/archive/kirisame"),
                ("Brunswick Underground Film Festival、ブランズウィック", None),
                ("Slow Forward #4、Indeks、バンドン\uff08ストリーミング\uff09", None),
            ]),
            ("2021年", [
                ("Videograms Film programme、Skalvijos kino centras、ビリニュス", "https://skalvija.lt/filmas/filmu-programa-troskimas-meile/?show=215793"),
                ("ワッタン映画祭「WFF-X film Screening」、ヤンゴン", "https://wffcinema.com/category_movies/61ae12ed925ae66dfe0e3095/movies"),
                ("Typography Center for Contemporary Art、クラスノダール", "http://typography-online.ru/2021/09/14/mieff-2/"),
                ("Garage Screen、モスクワ", "https://garagemca.org/en/event/special-screening-of-the-6th-moscow-international-experimental-film-festival-mieff-and-image-forum"),
                ("ミニキノフィルムウィーク：バリ国際短編映画祭", None),
                ("モスクワ国際実験映画祭", "https://mieff.com/program/crossroads_2021"),
                ("Sixteen Journal、パリ\uff08ストリーミング\uff09", "https://www.sixteenjournal.com/films/chiyo-by-chiemi-shimada/"),
                ("Dream, Dreaming, Dreamt、ウィニペグ\uff08ストリーミング\uff09", "https://www.winnipegfilmgroup.com/event/cabin-fever-dream-dreaming-dreamt-experimental-films-for-teens/"),
                ("Place M Film Festival、東京", "https://www.placemfilmfestival.tokyo/place-m-shorts"),
                ("hungry eyes festival、ギーセン", "https://hungryeyesfestival.de/das-festival"),
            ]),
            ("2020年", [
                ("Linea d\u2019Ombra Festival\u3000、サレルノ", "https://www.lineadombrafestival.it/lineadoc-film-in-concorso/"),
                ("dresdner schmalfilmtage、ドレスデン", "https://schmalfilmtage.de/en/program/"),
                ("Vdrome (ストリーミング)", "http://www.vdrome.org/chiemi-shimada/"),
                ("SeaShorts Film Festival、イポー", "https://seashorts.org/special-programme-space-in-between/"),
                ("ミニキノフィルムウィーク：バリ国際短編映画祭", "https://minikino.org/filmweek/mfw6/2020iff/"),
                ("ニッポンコネクション、フランクフルト", None),
                ("Form No Form (オンラインチャンネル)", "https://www.formnoform.com/"),
                ("アスワン国際女性映画祭", None),
                ("ロンドンショートフィルムフェスティバル", "https://shortfilms.org.uk/lsff2020/events/2020-01-14-documentary-the-measure-of-a-moment"),
            ]),
            ("2019年", [
                ("Place M Film Festival、東京", "https://film.placem.com/events/PlaceM_FilmFestival_2019.pdf"),
                ("V Festival de Video nodoCCS、\u3000バルセロナ", "https://mailchi.mp/e4a33b56c5ea/v_festival_video_nodoccs"),
                ("Unforeseen International Experimental Film Festival、\u3000ベルグラード", None),
                ("長岡芸術工事中、\u3000新潟", None),
                ("System of Care Season、Deptford Cinema、ロンドン", "http://deptfordcinema.org/new-events/americastollwhiteside2018"),
                ("サン・セバスティアン国際映画祭", "https://www.sansebastianfestival.com/2019/sections_and_films/nest_film_students/8/in"),
                ("日本アヴァンギャルド映画祭、ロンドン", "https://www.closeupfilmcentre.com/film_programmes/2019/jaeff-nation"),
                ("イメージフォーラムフェスティバル、東京、名古屋、京都", "http://www.imageforumfestival.com/bosyu2019/en.html"),
                ("Open City Documentary Festival、ロンドン", "https://opencitylondon.com/events/shorts-i-have-seen-nothing-i-have-seen-all/"),
                ("Wilden: Mekas, Menken, Rindland, and Shimada at Wolf Kino、ベルリン", None),
                ("シェフィールド国際ドキュメンタリー映画祭", None),
                ("ニッポン・コネクション、フランクフルト", None),
                ("ヨーロピアンメディアアートフェスティバル、オスナブリュック", None),
            ]),
            ("2018年", [("Stop Play Record Playback festival、\u3000ICA、ロンドン", None)]),
            ("2017年", [
                ("アップ＆カミング国際映画祭、\u3000ハノーファー", None),
                ("エステティカ短編映画祭、\u3000ヨーク", None),
                ("REC映画祭、ベルリン", None),
            ]),
            ("2016年", [
                ("Stop Play Record スクリーニング、ICA、ロンドン", None),
                ("Chiaroscuro International Film Series、Urban Institute for Contemporary Arts、ミシガン", None),
            ]),
        ]),
        ("賞、助成、レジデンシー", [
            ("2024年", [("Developing your Creative Practice、Arts Council England", None)]),
            ("2023年", [("Connections Through Culture助成プログラム、British Council", None)]),
            ("2022年", [
                ("Monographs ショートフィルムコミッション、Asian Film Archive、シンガポール", None),
                ("Primary Residency Prize、NAE Open、ノッティンガム", None),
            ]),
            ("2021年", [("山形ドキュメンタリー道場\uff08オンラインレジデンシー\uff09", None)]),
            ("2020年", [
                ("Matsudo \u201cQOL\u201d Residency Award、PARADISE AIR、松戸", None),
                ("ロカレン・ファンデーション レジデンシー、リヒテンフォールデ", None),
            ]),
            ("2019年", [("ベストUK短編映像アワードノミネート、Open City Documentary Festival、ロンドン", None)]),
            ("2018年", [("学生CGコンテスト アート部門 優秀賞、東京", None)]),
            ("2015年", [("Stop Play Record コミッション、ICA、キングストン大学、Arts Council England、ロンドン", None)]),
        ]),
        ("学歴", [
            ("2022-2024年", [("School of the Damned", None)]),
            ("2022-2023年", [("LUX Critical Forum", None)]),
            ("2017-2019年", [("キングストン大学大学院美術学部実験映像専攻\u3000修士課程修了 (Distinction)", None)]),
            ("2015-2016年", [("グランドバレー州立大学 交換留学プログラム", None)]),
            ("2013-2017年", [("キングストン大学美術学部映像製作学科卒業 (First Class)", None)]),
        ]),
        ("インターン", [
            ("2019年", [
                ("Alia Syedの元でポストプロダクションアシスタント", None),
                ("Ben Riversの元でアシスタント", None),
            ]),
        ]),
        ("トーク", [
            ("2020年", [("ロンドンショートフィルムフェスティバル インダストリーパネル: Articulating Diaspora、Rich Mix、ロンドン", None)]),
            ("2019年", [
                ("フィルムメーカーズ ワークショップ、MetFilm School、日本アヴァンギャルド映画祭、ロンドン", None),
                ("アーティストトーク、キングストン大学、ロンドン", None),
            ]),
        ]),
    ],
    interviews_title="インタビュー、レビュー",
    interviews=[
        ("Vdrome「ちよ」インタビュー\uff08インタビュアー：Peter Taylor\uff09", "https://www.vdrome.org/chiemi-shimada"),
        ("Phil Coldironによる「ちよ」レビュー", "https://philcoldiron.substack.com/p/chiyo?s=r"),
        ("Asian Movie Pulse「ちよ」インタビュー", "https://asianmoviepulse.com/2019/10/interview-with-chiemi-shimada-i-think-the-borders-between-cinema-and-video-art-are-getting-blurred/"),
        ("Asian Movie Pulse「ちよ」レビュー", "https://asianmoviepulse.com/2020/03/short-film-review-chiyo-2019-by-chiemi-shimada/"),
        ("Japanese experimental documentary now\uff08一部「ちよ」レビュー\uff09", "https://www.bfi.org.uk/news-opinion/sight-sound-magazine/features/japanese-experimental-documentary-now-sheffield-docfest-2019"),
        ("Aspiring filmmakers at Kingston University given chance to step into the spotlight through Channel 4 programme Random Acts", "https://www.kingston.ac.uk/news/article/1805/08-mar-2017-aspiring-filmmakers-at-kingston-university-given-chance-to-step-into-the-spotlight-through-channel-4/"),
    ],
)


def render_cv_column(sections, interviews_title, interviews, lang_attr=""):
    out = f'    <div class="cv-col"{lang_attr}>\n'
    for title, years in sections:
        out += f'      <div class="cv-section"><h2>{title}</h2><div class="history-list">\n'
        for year, items in years:
            lis = "\n".join(
                f'              <li><a href="{url}" target="_blank" rel="noopener">{text}</a></li>' if url
                else f'              <li>{text}</li>'
                for text, url in items
            )
            out += f'          <div class="history-year">\n            <div class="y">{year}</div>\n            <ul>\n{lis}\n            </ul>\n          </div>\n'
        out += "      </div></div>\n"
    out += f'      <div class="cv-section" style="margin-bottom:0;"><h2>{interviews_title}</h2><div class="history-list">\n        <div class="history-year">\n          <div class="y">&nbsp;</div>\n          <ul>\n'
    for text, url in interviews:
        out += f'            <li><a href="{url}" target="_blank" rel="noopener">{text}</a></li>\n' if url else f'            <li>{text}</li>\n'
    out += "          </ul>\n        </div>\n      </div></div>\n"
    out += "    </div>\n"
    return out


def build_cv_page():
    html = head("CV \u2014 Chiemi Shimada", "Exhibitions, screenings, awards, education and press for artist and filmmaker Chiemi Shimada.")
    html += header("cv.html")
    html += """
  <main>
    <div class="cv-head wrap">
      <h1>CV</h1>
      <p class="place">"""
    html += CV["place"]
    html += """</p>
"""
    for para in CV["bio"]:
        html += f"      <p class=\"bio\">{para}</p>\n"
    contact_links = "\n        ".join(f'<a href="{href}" target="_blank" rel="noopener">{label}</a>' for label, href in CV["contact"])
    html += f"""      <div class="contact">
        {contact_links}
      </div>
    </div>

    <div class="cv-columns wrap">
"""
    html += render_cv_column(CV["sections"], "Interviews & Reviews", CV["interviews"], lang_attr=' lang="en"')
    html += render_cv_column(CV_JA["sections"], CV_JA["interviews_title"], CV_JA["interviews"], lang_attr=' lang="ja"')
    html += "    </div>\n  </main>\n"
    html += footer()
    html += "</body>\n</html>\n"
    return html


SOCIAL = [
    ("Instagram", "https://www.instagram.com/smdcem/"),
    ("Vimeo", "https://vimeo.com/chiemis"),
    ("Email", "mailto:chi00shi00@gmail.com"),
]


def header(active_href, depth=""):
    links = "\n      ".join(
        f'<a href="{depth}{href}"{" class=\"is-active\"" if href == active_href else ""}>{label}</a>'
        for label, href in NAV
    )
    return f"""  <header class="site-header">
    <div class="bar"><a class="mark" href="{depth}index.html">Chiemi Shimada</a></div>
  </header>
  <nav class="site-nav">
      {links}
  </nav>
"""


def footer(depth=""):
    social = "\n        ".join(f'<a href="{href}" target="_blank" rel="noopener">{label}</a>' for label, href in SOCIAL)
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="social">
        {social}
      </div>
      <p class="copy">&copy; Chiemi Shimada</p>
    </div>
  </footer>
"""


def head(title, description, depth=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{depth}css/style.css">
</head>
<body>
"""


def media_block(p):
    out = ""
    if p.get("video_id"):
        out += f"""    <div class="video-embed">
      <iframe src="https://www.youtube.com/embed/{p['video_id']}" title="{p['title']}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
"""
    frames = "\n".join(
        f'      <div class="media-frame"><!-- replace with <img src="../images/{p["slug"]}-0{i+1}.jpg" alt=""> or a Vimeo embed -->Image {i+1}</div>'
        for i in range(p["media_count"])
    )
    out += f"""    <div class="media-grid">
{frames}
    </div>
"""
    for cap in p["media_captions"]:
        out += f'    <p class="caption">{cap}</p>\n'
    return out


def credits_block(p):
    if not p["credits"]:
        return ""
    rows = "\n".join(
        f'      <div><span class="role">{role}:</span> {names}</div>' for role, names in p["credits"]
    )
    return f"""    <h3 class="block-title">Credits</h3>
    <div class="credits">
{rows}
    </div>
"""


def history_block(p):
    if not p["history"]:
        return ""
    title = p.get("history_title") or "Exhibition History"
    years = ""
    for year, items in p["history"]:
        lis = "\n".join(
            f'          <li><a href="{url}" target="_blank" rel="noopener">{text}</a></li>' if url
            else f'          <li>{text}</li>'
            for text, url in items
        )
        years += f"""      <div class="history-year">
        <div class="y">{year}</div>
        <ul>
{lis}
        </ul>
      </div>
"""
    return f"""    <h3 class="block-title">{title}</h3>
    <div class="history-list">
{years}
    </div>
"""


def build_project_page(p, prev_p, next_p):
    desc_html = "\n".join(f"    <p>{d}</p>" for d in p["desc"])
    original_html = ""
    if p["original_text"]:
        paras = "\n".join(f"      <p>{t}</p>" for t in p["original_text"])
        original_html = f'    <div class="original-text">\n{paras}\n    </div>\n'

    meta_bits = [p["year"], p["medium"], p["duration"]]
    meta_bits = [m for m in meta_bits if m]
    meta = ", ".join(meta_bits)

    jp_html = f'<p class="jp-title">{p["jp_title"]}</p>\n' if p["jp_title"] else ""

    html = head(f'{p["title"]} {p["subtitle"]} \u2014 Chiemi Shimada'.strip(), p["medium"], depth="../")
    html += header(f'projects/{p["slug"]}.html', depth="../")
    html += f"""
  <main>
    <div class="wrap project-head">
      <a class="backlink" href="../index.html">&larr; Back to works</a>
      <h1>{p["title"]} {f'<span class="sub">{p["subtitle"]}</span>' if p["subtitle"] else ""}</h1>
      {jp_html}      <p class="meta-line">{meta}</p>
    </div>
    <div class="wrap project-body">
{desc_html}
{original_html}{media_block(p)}{credits_block(p)}{history_block(p)}
      <div class="proj-nav">
        <a href="{prev_p}"><span class="dir">Previous</span>&larr; {PROJECT_TITLE.get(prev_p, 'Works')}</a>
        <a class="next" href="{next_p}"><span class="dir">Next</span>{PROJECT_TITLE.get(next_p, 'Works')} &rarr;</a>
      </div>
    </div>
  </main>
"""
    html += footer(depth="../")
    html += "</body>\n</html>\n"
    return html


PROJECT_TITLE = {}


def main():
    slugs = [p["slug"] for p in PROJECTS]
    for i, p in enumerate(PROJECTS):
        PROJECT_TITLE[f"{p['slug']}.html"] = p["title"]
    PROJECT_TITLE["../index.html"] = "Home"

    os.makedirs(os.path.join(ROOT, "projects"), exist_ok=True)

    for i, p in enumerate(PROJECTS):
        prev_slug = slugs[i - 1] + ".html" if i > 0 else "../index.html"
        next_slug = slugs[i + 1] + ".html" if i < len(slugs) - 1 else "../index.html"
        html = build_project_page(p, prev_slug, next_slug)
        with open(os.path.join(ROOT, "projects", f"{p['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(html)

    with open(os.path.join(ROOT, "cv.html"), "w", encoding="utf-8") as f:
        f.write(build_cv_page())

    print(f"Generated {len(PROJECTS)} project pages + cv.html.")


if __name__ == "__main__":
    main()
