from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import InputRequired, NumberRange
import requests

professions = [
    'Alchemy',
    'Blacksmithing',
    'Cooking',
    'Enchanting',
    'Engineering',
    'Jewelcrafting',
    'Leatherworking',
    'Tailoring']

# Fetch server list
response = requests.get("https://api.nexushub.co/wow-classic/v1/servers/full/")
responseJson = response.json()

servers = dict()
for line in responseJson:
    servers[line["slug"]] = line["name"]

class UserInputForm(FlaskForm):
    server = SelectField(u'Server',
        default='gehennas',
        choices=[(slug, name) for slug, name in servers.items()])
    faction = SelectField(u'Faction',
        default='horde',
        choices=[('alliance', 'Alliance'), ('horde', "Horde")])
    profession = SelectField(u'Profession',
        choices=[(profession, profession) for profession in professions])
    startSkill = IntegerField(u'Starting skill',
        default=1,
        validators=[InputRequired(),
                    NumberRange(min=1, max=374)])
    targetSkill = IntegerField(u'Target skill',
        default=375,
        validators=[InputRequired(),
                    NumberRange(min=2, max=375)])
    phase = SelectField(u'Phase',
        default='5',
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    calculate = SubmitField('Calculate')
    includeVendor = BooleanField(u'Vendor', default="checked")
    includeVendorLimited = BooleanField(u'VendorLimited', default="checked")
    includeDrop = BooleanField(u'Drop')
    includeQuest = BooleanField(u'Quest')
    includeReputation = BooleanField(u'Reputation')
    includeSeasonal = BooleanField(u'Seasonal')

    # https://github.com/ItsMonkk/WowProfessionLevelingTool/commit/40431fb6654ba5de61fd536ca022c26be7369d7b
    difficulty = RadioField(u'Difficulty:',
        choices=[("Green", "Green"), 
            ("Yellow", "Yellow"), 
            ("Orange", "Orange")],
        default="Green")

    blacksmithingSchool = RadioField(u'School:',
        choices=[("None", "None"),
                ("Armorsmithing", "Armorsmithing"),
                ("Weaponsmithing", "Weaponsmithing")],
        default="None")
    engineeringSchool = RadioField(u'School:',
        choices=[("None", "None"),
                ("Gnomish", "Gnomish"),
                ("Goblin", "Goblin")],
        default="None")
    leatherworkingSchool = RadioField(u'School:',
        choices=[("None", "None"),
                 ("Dragonscale", "Dragonscale"),
                 ("Elemental", "Elemental"),
                 ("Tribal", "Tribal")],
        default="None")
    enchantingRods = BooleanField(u'Include enchanting rods', default="checked")