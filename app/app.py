# imports
import random
import openai
import os
import json
from flask import Flask, render_template, request, redirect

# variables
app = Flask(__name__, template_folder='templateFiles',
            static_folder='staticFiles')
port = 5000

# functions
def read_secrets(file) -> dict:
    filename = os.path.join(file)
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def view_health():
    # generate html code
    return render_template('health.html')

def get_character_description(prompt, openai_api_key):
    # Set the API key
    openai.api_key = openai_api_key

    # Set the request data
    model_engine = "text-davinci-002"
    prompt = (f"{prompt}\n")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,  # higher supports larger output
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completions.choices[0].text

def select_character_name(gender):
    male_names = ['Arndt', 'Bartolf', 'Carsten', 'Dorn',
                  'Eberhard', 'Fabian', 'Gernot', 'Hagen', 'Ingolf', 'Jörg']
    female_names = ['Adelheid', 'Beatrice', 'Carla', 'Dorothea',
                    'Elke', 'Friederike', 'Gisela', 'Hildegard', 'Ingrid', 'Johanna']

    if gender == "male":
        name = random.choice(male_names)
    elif gender == "female":
        name = random.choice(female_names)
    elif gender == "any":
        all_names = male_names + female_names
        name = random.choice(all_names)
    return name

def select_character_race():
    races = ['Mensch', 'Elf', 'Zwerg', 'Halbelf',
             'Halbling', 'Ork', 'Troll', 'Goblin', 'Nachelfen']
    return random.choice(races)

def select_character_profession():
    professions = ['Krieger', 'Magier', 'Dieb', 'Druide', 'Barden', 'Priester']
    return random.choice(professions)

def select_character_trait(count):
    positiv_traits = [
        'abenteuerlustig', 'achtsam', 'aktiv', 'akribisch', 'ambitioniert', 'anpassungsfähig', 'aufgeschlossen', 'außergewöhnlich', 'autark',
        'barmherzig', 'begeisterungsfähig', 'behutsam', 'belastbar', 'bemüht', 'bescheiden', 'bodenständig',
        'clever', 'charismatisch', 'charmant',
        'durchsetzungsfähig', 'direkt', 'dankbar', 'diszipliniert',
        'ehrgeizig', 'effizient', 'ehrlich', 'einfühlsam', 'einsichtig', 'eloquent', 'entschlossen', 'eigeninitiativ', 'energievoll', 'enthusiastisch',
        'freundlich', 'flexibel', 'fröhlich', 'feinfühlig', 'fürsorglich', 'furchtlos', 'fair',
        'geduldig', 'gelassen', 'gesellig', 'gütig', 'großzügig', 'gewissenhaft', 'gefühlvoll', 'geistreich', 'gerecht',
        'hilfsbereit', 'höflich', 'humorvoll', 'herzlich',
        'ideenreich', 'innovativ', 'intelligent', 'integer',
        'jugendlich', 'jäckisch',
        'kontaktfreudig', 'kollegial', 'kommunikativ', 'kompetent', 'konfliktfähig', 'kritikfähig', 'konstruktiv', 'klug', 'kreativ', 'konsequent',
        'lebensbejahend', 'leidenschaftlich', 'lernwillig', 'liebend', 'loyal', 'leistungsorientiert', 'lösungsorientiert',
        'motiviert', 'mutig', 'mitdenkend', 'mitreißend',
        'natürlich', 'nachsichtig', 'naturverbunden', 'nett', 'neugierig',
        'optimistisch', 'offen', 'organisiert', 'ordentlich', 'originell',
        'positiv', 'pragmatisch', 'pflichtbewusst', 'passioniert', 'präzise', 'produktiv',
        'qualifiziert',
        'ruhig', 'risikobereit', 'redegewandt', 'reflektierend', 'respektvoll', 'rücksichtsvoll', 'relaxed', 'raffiniert', 'robust',
        'selbstlos', 'selbstständig', 'selbstbestimmt', 'selbstreflektierend', 'sensibel', 'sinnlich', 'sorgfältig', 'solide', 'souverän', 'spontan', 'stark', 'strebsam', 'strukturiert', 'schlagfertig',
        'tolerant', 'teamfähig', 'talentiert', 'temperamentvoll', 'tiefgründig',
        'unabhängig', 'unnachgiebig', 'unbeschwert', 'unbeirrbar', 'unkompliziert', 'unterhaltsam', 'unermüdlich', 'umgänglich',
        'verantwortungsbewusst', 'vertrauenswürdig', 'vielseitig', 'verständnisvoll', 'vorausschauend',
        'wortgewandt', 'warmherzig', 'weltoffen', 'willensstark', 'wissbegierig', 'weise',
    ]
    # https://www.jolie.de/leben/negative-charaktereigenschaften-so-kannst-du-sie-ablegen-210383.html#210383_3d3a08_Negative_Charaktereigenschaften_Liste_von_A_bis_Z
    negativ_traits = [
        'arrogant', 'aggressiv', 'abgehoben', 'abhängig', 'abweisend', 'angeberisch', 'aufdringlich', 'aufsässig', 'ängstlich',
        'bedrohlich', 'beeinflussbar', 'belehrend', 'berechnend', 'besitzergreifend', 'besserwisserisch', 'biestig', 'bösartig',
        'chauvinistisch', 'charakterlos', 'cholerisch',
        'dämlich', 'derb', 'desinteressiert', 'destruktiv', 'devot', 'dickköpfig', 'diskriminierend', 'dreist', 'dünnhäutig', 'durchtrieben',
        'egoistisch', 'eigenartig', 'einfallslos', 'eiskalt', 'engstirnig', 'entscheidungsunfähig', 'erbarmungslos',
        'falsch', 'faul', 'fies', 'feindselig',
        'gefühlskalt', 'gefühlsduselig', 'gehässig', 'geldgierig', 'geschwätzig', 'gemein', 'gewissenlos', 'gnadenlos', 'griesgrämig',
        'habsüchtig', 'harsch', 'heimtückisch', 'herablassend', 'heuchlerisch', 'hinterhältig', 'hitzköpfig', 'hochnäsig',
        'ignorant', 'illoyal', 'inkonsequent', 'intolerant', 'irrational', 'ichbezogen',
        'jähzornig', 'jasagerisch',
        'kleinkariert', 'kleinlich', 'knauserig', 'kommunikationsunfähig', 'kompromisslos', 'konfliktscheu', 'kratzbürstig', 'kritikunfähig',
        'langweilig', 'launisch', 'lieblos', 'lügnerisch', 'lustlos',
        'machthaberisch', 'manipulativ', 'maßlos', 'miesepetrig', 'missgünstig', 'mürrisch', 'mutlos',
        'nachtragend', 'negativ', 'nervig', 'niveaulos', 'neidisch',
        'oberflächlich', 'obsessiv', 'ordinär',
        'pietätlos', 'plump', 'prahlerisch', 'prollig', 'primitiv',
        'quengelig', 'querulantisch',
        'rabiat', 'rachsüchtig', 'realitätsfern', 'rechthaberisch', 'redselig', 'reizbar', 'respektlos', 'rücksichtslos', 'ruppig',
        'sarkastisch', 'schadenfroh', 'schamlos', 'schluderig', 'schroff', 'schwerfällig', 'selbstdarstellerisch', 'selbstverliebt', 'sentimental', 'streitsüchtig',
        'taktlos', 'töricht', 'trödelig', 'trotzig', 'tüddelig',
        'überempfindlich', 'überheblich', 'unaufrichtig', 'unbeholfen', 'unbelehrbar', 'undankbar', 'unehrlich', 'unfair', 'unfreundlich', 'unglaubwürdig', 'unkonzentriert', 'unpünktlich',
        'verantwortungslos', 'verbittert', 'verletzend', 'verlogen', 'verständnislos', 'verwöhnt', 'voreingenommen', 'vorlaut',
        'waghalsig', 'wankelmütig', 'wehmütig', 'wichtigtuerisch', 'widersprüchlich', 'willensschwach',
        'zaghaft', 'zerstörerisch', 'ziellos', 'zweifelnd',
    ]
    all_character_traits = positiv_traits + negativ_traits
    return random.sample(all_character_traits, count)

def generate_character_attributes():
    attrib_start = 5
    attrib_end = 18
    attributes = {
        'Stärke': random.randint(attrib_start, attrib_end),
        'Geschicklichkeit': random.randint(attrib_start, attrib_end),
        'Intuition': random.randint(attrib_start, attrib_end),
        'Charisma': random.randint(attrib_start, attrib_end),
        'Konstitution': random.randint(attrib_start, attrib_end),
        'Intelligenz': random.randint(attrib_start, attrib_end),
        'Willenskraft': random.randint(attrib_start, attrib_end),
        'Stärke': random.randint(attrib_start, attrib_end),
        'Stärke': random.randint(attrib_start, attrib_end),
    }
    return attributes

# code
secrets = read_secrets('secrets.json')

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('base.html')
    # return redirect("/generate")

@app.route('/description', methods=['GET'])
def description():
    prompt = "wie ist das wetter heute?"
    return render_template('description.html', text=get_character_description(openai_api_key=secrets["openai_api_key"], prompt=prompt))

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    character = {
        "name": select_character_name("any"),
        "race": select_character_race(),
        "profession": select_character_profession(),
        "traits": select_character_trait(5),
        "attributes": generate_character_attributes()
    }

    if request.method == 'POST':
        if request.form.get('action_regenerate') == 'erneut generieren"':
            html = render_template(
                'character.html', form=request.form, character=character)
        elif request.form.get('action_generate_description') == 'Charakterbeschreibung generieren':
            html = render_template('health.html')
    elif request.method == 'GET':
        html = render_template(
            'character.html', form=request.form, character=character)

    # generate html code
    return html

@app.route('/health')
def health():
    return view_health()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)