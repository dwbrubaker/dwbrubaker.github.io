from pybtex.database.input import bibtex

def emoji_icon(emoji, size):
    return f"""<span style="font-size:{size}; vertical-align:middle;" aria-hidden="true">&#x{emoji};</span>"""

def get_personal_data():
    name = ["Daniel", "Brubaker"]
    email = "dwb60 [at] georgetown [dot] edu"
    github = "Whilsun"
    linkedin = "Daniel-Brubaker"

    bio_text = f"""
                <p>
                    Howdy! I am a computational linguist interested in discourse and semantics. 
                    My work focuses on using LMs to better understand about how people use language.
                    
                </p>
                
                <p>
                    I am currently a PhD student at Georgetown University, advised by <a href="https://gucorpling.org/amir/">Amir Zeldes</a>. 
                    Prior to that, I earned my BA and BS in Linguistics and Computer Science respectively from UT Austin, where I worked with <a href="https://jessyli.com/">Jessy Li</a> and <a href="https://kanishka.website/">Kanishka Misra</a>.
                </p>

                <p>
                    When I'm not thinking about lanugage, I like to play the electric bass, go out into nature, and read books. My favorite national parks are Death Valley and Joshua Tree, and my favorite book is Frankenstein by Mary Shelley. I'm also a big fan of Emoji 🌃
                </p>

                <p>
                    <a href="mailto:dwb60@georgetown.edu" style="margin-right: 5px;"> {emoji_icon("1F4E7", "1.3em")} <span style="vertical-align: middle;"><b>Mail</b></span></a>
                    <a href="https://dwbrubaker.github.io/assets/pdf/Daniel_Brubaker_Resume.pdf" target="_blank" style="margin-right: 5px">{emoji_icon("1F4C4", "1.3em")} <span style="vertical-align: middle;"><b>Resumé</b></span></a>
                    <a href="https://github.com/whilsun" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg" style="vertical-align: middle;"></i> <span style="vertical-align: middle;"><b>Github</b></span></a>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#trivia" data-toggle="collapse" style="margin-left: -15px; margin-top: -2px;">{emoji_icon("1F996","1.3em")}<b>Trivia</b></button>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#links" data-toggle="collapse" style="margin-left: -25px; margin-top: -2px;">{emoji_icon("1F517","1.3em")}<b>Links</b></button>
                    
                    
                    <div id="trivia" class="collapse" style="background: #cee0fd">
                    <span style="font-weight: bold;"></span>
                    Under Construction!🏗️
                    <!--The infinity emoji ♾️'s official name is U+267E PERMANENT PAPER SIGN, denoting acid-free paper. Without the variation selector that presents it as an emoji, it looks like this: ♾ -->
                    </div>

                    <div id="links" class="collapse" style="background: #ead4f7">
                    <span style="font-weight: bold;"></span>
                    Under Construction!🏗️
                    </div>

                    <!--
                    <a href="https://m-Brubaker.github.io/assets/other/bio.txt" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-graduation-cap"></i> Bio</a>
                    <a href="mailto:micBrubaker1@gmail.com" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/Mi_Brubaker" target="_blank" style="margin-right: 5px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=v1O7i_0AAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://www.linkedin.com/in/Daniel-Brubaker" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    -->
                </p>
    """
    footer = """
            <div class="col-sm-12">
                <h3></h3>
                <div style="font-style: italic; color: #555555;">
                    <p>
                        Based on a template by <a href="https://github.com/m-niemeyer/m-niemeyer.github.io">Michael Niemeyer</a>.
                    </p>
                    <p style="margin-top:-15px"> 
                        All content is human-generated. 
                    </p>
                </div>
            </div>
    """
    return name, bio_text, footer


def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Daniel Brubaker', add_links=True):
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.first_names + p.middle_names + p.last_names: 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-0"></div>"""
    # s=""
    s += """<div class="col-sm-10">"""

    link = "url" if "url" in entry.fields.keys() else "html"


    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields[link]}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields[link]}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    # artefacts = {'url': 'Paper', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    # i = 0
    # for (k, v) in artefacts.items():
    #     if k in entry.fields.keys():
    #         if i > 0:
    #             s += ' / '
    #         s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
    #         i += 1
    #     else:
    #         print(f'[{entry_key}] Warning: Field {k} missing!')

    # cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    # cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    # for entr in ['title', 'booktitle', 'year']:
    #     cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    # cite += """}</pre></code>"""
    # s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Doppio+One&display=swap" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Doppio+One&family=Sora:wght@100..800&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/bitmaks/cm-web-fonts@latest/fonts.css">

  <style>
  
    h1 {{
    font-family: 'Doppio One', sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #222;
    }}

    body {{
        font-family: 'Sora', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #222;
        }}
    </style>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h1 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]} &#x1F320;</h1>
                    </div>

                    <br>
                    <div class="col-md-9 order-2 order-md-1" >
                        {bio_text}
                    </div>
                 

                <div class="col-md-3 order-1 order-md-2 mb-3 mb-md-0">
                    <figure class="text-center m-0">
                        <img src="assets/img/dbrubaker.jpg"
                            alt="A profile picture of Daniel Brubaker smiling, in a hawaiian shirt and C-SPAN hat, standing in front of Healy Hall at Georgetown University."
                            style="border: 3px solid #555; border-radius: 3px; width: 280px; max-width: 100%;">
                        <figcaption style="font-family: 'Computer Modern Serif', serif; max-width: 280px; margin: 0.5rem auto 0;">
                            <strong>Figure 1.</strong> Daniel Brubaker
                        </figcaption>
                    </figure>
                </div>

                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" >
                        <h4>Publications &#x1F4DC;</h4>
                        {pub}
                    </div>
                </div>
                <!--
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" >
                        <h4>Talks</h4>
                        {talks}
                    </div>
                </div>
                -->
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
            <div class="col-md-1"></div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
