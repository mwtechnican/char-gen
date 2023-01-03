# from random import randint, choice
import random
from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
port = 5000

@app.route('/')
def generate_character():
    # Name 
    male_names =['Arndt', 'Bartolf', 'Carsten', 'Dorn','Eberhard','Fabian','Gernot','Hagen','Ingolf','Jörg']
    female_names = ['Adelheid', 'Beatrice', 'Carla', 'Dorothea', 'Elke', 'Friederike', 'Gisela', 'Hildegard', 'Ingrid', 'Johanna']
    all_names = male_names + female_names
    name = random.choice(all_names)

    # Rasse
    races =['Mensch', 'Elf', 'Zwerg', 'Halbelf', 'Halbling', 'Ork','Troll', 'Goblin', 'Nachelfen']
    race = random.choice(races)

    # Beruf
    professions = ['Krieger', 'Magier', 'Dieb', 'Druide', 'Barden', 'Priester']
    profession = random.choice(professions)

    # Attribute
    attributes = ['Stärke', 'Geschicklichkeit', 'Intuition', 'Charisma', 'Konstitution', 'Intelligenz', 'Willenskraft']
    attribute_values = {}
    for attribute in attributes:
        attribute_values[attribute] = random.randint(8, 18)

    # Character traits
    # https://www.jolie.de/leben/positive-charaktereigenschaften-liste-von-bis-z-210373.html#210373_2a6bae_Positive_Charaktereigenschaften_Liste_von_A_bis_Z
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
    character_traits = random.sample(all_character_traits, 3)

    # generate html code
    return render_template('character.html', attributes=attributes, attribute_values=attribute_values, profession=profession, race=race, name=name, character_traits=character_traits)

@app.route('/health')
def generate_health():

    # generate html code
    return render_template('health.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)