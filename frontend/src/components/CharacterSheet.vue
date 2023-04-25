<template>
    <div>
        <form @submit.prevent="submitForm">
            <!-- Basic Info -->
            <h2>Basic Info</h2>
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" v-model="character.name" required>
            </div>
            <div class="form-group">
                <label for="class">Class:</label>
                <select id="class" v-model="character.class" required>
                    <option disabled value="">Please select one</option>
                    <option v-for="{ cls, index } in classes" :key="index" :value="cls">{{ cls }}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="race">Race:</label>
                <select id="race" v-model="character.race" required>
                    <option disabled value="">Please select one</option>
                    <option v-for="{ race, index } in races" :key="index" :value="race">{{ race }}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="background">Background:</label>
                <select id="background" v-model="character.background" required>
                    <option disabled value="">Please select one</option>
                    <option v-for="{ bg, index } in backgrounds" :key="index" :value="bg">{{ bg }}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="alignment">Alignment:</label>
                <select id="alignment" v-model="character.alignment" required>
                    <option disabled value="">Please select one</option>
                    <option v-for="{ alignment, index } in alignments" :key="index" :value="alignment">{{ alignment }}
                    </option>
                </select>
            </div>

            <!-- Ability Scores -->
            <h2>Ability Scores</h2>
            <div class="form-group">
                <label for="strength">Strength:</label>
                <input type="number" id="strength" v-model="character.abilityScores.strength" min="1" max="20" required>
            </div>
            <div class="form-group">
                <label for="dexterity">Dexterity:</label>
                <input type="number" id="dexterity" v-model="character.abilityScores.dexterity" min="1" max="20" required>
            </div>
            <div class="form-group">
                <label for="constitution">Constitution:</label>
                <input type="number" id="constitution" v-model="character.abilityScores.constitution" min="1" max="20"
                    required>
            </div>
            <div class="form-group">
                <label for="intelligence">Intelligence:</label>
                <input type="number" id="intelligence" v-model="character.abilityScores.intelligence" min="1" max="20"
                    required>
            </div>
            <div class="form-group">
                <label for="wisdom">Wisdom:</label>
                <input type="number" id="wisdom" v-model="character.abilityScores.wisdom" min="1" max="20" required>
            </div>
            <div class="form-group">
                <label for="charisma">Charisma:</label>
                <input type="number" id="charisma" v-model="character.abilityScores.charisma" min="1" max="20" required>
            </div>

            <!-- Skills -->
            <h2>Skills</h2>
            <div class="form-group">
                <label for="acrobatics">Acrobatics (Dex):</label>
                <input type="checkbox" id="acrobatics" v-model="character.skills.acrobatics">
            </div>
            <div class="form-group">
                <label for="animal-handling">Animal Handling (Wis):</label>
                <input type="checkbox" id="animal-handling" v-model="character.skills.animalHandling">
            </div>
            <div class="form-group">
                <label for="arcana">Arcana (Int):</label>
                <input type="checkbox" id="arcana" v-model="character.skills.arcana">
            </div>
            <div class="form-group">
                <label for="athletics">Athletics (Str):</label>
                <input type="checkbox" id="athletics" v-model="character.skills.athletics">
            </div>
            <div class="form-group">
                <label for="deception">Deception (Cha):</label>
                <input type="checkbox" id="deception" v-model="character.skills.deception">
            </div>
            <div class="form-group">
                <label for="history">History (Int):</label>
                <input type="checkbox" id="history" v-model="character.skills.history">
            </div>
            <div class="form-group">
                <label for="insight">Insight (Wis):</label>
                <input type="checkbox" id="insight" v-model="character.skills.insight">
            </div>
            <div class="form-group">
                <label for="intimidation">Intimidation (Cha):</label>
                <input type="checkbox" id="intimidation" v-model="character.skills.intimidation">
            </div>
            <div class="form-group">
                <label for="investigation">Investigation (Int):</label>
                <input type="checkbox" id="investigation" v-model="character.skills.investigation">
            </div>
            <div class="form-group">
                <label for="medicine">Medicine (Wis):</label>
                <input type="checkbox" id="medicine" v-model="character.skills.medicine">
            </div>
            <div class="form-group">
                <label for="nature">Nature (Int):</label>
                <input type="checkbox" id="nature" v-model="character.skills.nature">
            </div>
            <div class="form-group">
                <label for="perception">Perception (Wis):</label>
                <input type="checkbox" id="perception" v-model="character.skills.perception">
            </div>
            <div class="form-group">
                <label for="performance">Performance (Cha):</label>
                <input type="checkbox" id="performance" v-model="character.skills.performance">
            </div>
            <div class="form-group">
                <label for="persuasion">Persuasion (Cha):</label>
                <input type="checkbox" id="persuasion" v-model="character.skills.persuasion">
            </div>
            <div class="form-group">
                <label for="religion">Religion (Int):</label>
                <input type="checkbox" id="religion" v-model="character.skills.religion">
            </div>
            <div class="form-group">
                <label for="sleight-of-hand">Sleight of Hand (Dex):</label>
                <input type="checkbox" id="sleight-of-hand" v-model="character.skills.sleightOfHand">
            </div>
            <div class="form-group">
                <label for="stealth">Stealth (Dex):</label>
                <input type="checkbox" id="stealth" v-model="character.skills.stealth">
            </div>
            <div class="form-group">
                <label for="survival">Survival (Wis):</label>
                <input type="checkbox" id="survival" v-model="character.skills.survival">
            </div>
            <!-- Equipment -->
            <h2>Equipment</h2>
            <div class="form-group">
                <label for="armor">Armor:</label>
                <select id="armor" v-model="character.equipment.armor">
                    <option disabled value="">Please select one</option>
                    <option v-for="{item, index} in armor" :key="index" :value="item">{{ item }}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="weapon">Weapon:</label>
                <select id="weapon" v-model="character.equipment.weapon">
                    <option disabled value="">Please select one</option>
                    <option v-for="{item, index} in weapons" :key="index" :value="item">{{ item }}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="other-equipment">Other Equipment:</label>
                <textarea id="other-equipment" v-model="character.equipment.other"></textarea>
            </div>

            <!-- Spells -->
            <h2>Spells</h2>
            <div class="form-group">
                <label for="known-spells">Known Spells:</label>
                <textarea id="known-spells" v-model="character.spells.known"></textarea>
            </div>
            <div class="form-group">
                <label for="prepared-spells">Prepared Spells:</label>
                <textarea id="prepared-spells" v-model="character.spells.prepared"></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit">Submit</button>
        </form>
    </div>
</template>
<script>
export default {
    data() {
        return {
            classes: ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'],
            races: ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling'],
            backgrounds: ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin'],
            alignments: ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil'],
            armor: ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate', 'Half Plate', 'Ring Mail', 'Chain Mail', 'Splint', 'Plate'],
            weapons: ['Club', 'Dagger', 'Greatclub', 'Handaxe', 'Javelin', 'Light Hammer', 'Mace', 'Quarterstaff', 'Sickle', 'Spear', 'Light Crossbow', 'Dart', 'Shortbow', 'Sling', 'Battleaxe', 'Flail', 'Glaive', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'War Pick', 'Warhammer', 'Whip', 'Blowgun', 'Hand Crossbow', 'Heavy Crossbow', 'Longbow', 'Net'],
            character: {
                name: '',
                class: '',
                race: '',
                background: '',
                alignment: '',
                abilityScores: {
                    strength: '',
                    dexterity: '',
                    constitution: '',
                    intelligence: '',
                    wisdom: '',
                    charisma: ''
                },
                skills: {
                    acrobatics: false,
                    animalHandling: false,
                    arcana: false,
                    athletics: false,
                    deception: false,
                    history: false,
                    insight: false,
                    intimidation: false,
                    investigation: false,
                    medicine: false,
                    nature: false,
                    perception: false,
                    performance: false,
                    persuasion: false,
                    religion: false,
                    sleightOfHand: false,
                    stealth: false,
                    survival: false
                },
                equipment: {
                    armor: '',
                    weapon: '',
                    other: ''
                },
                spells: {
                    known: '',
                    prepared: ''
                }
            }
        }
    },
    methods: {
        submitForm() {
            console.log(this.character);
        }
    }
}
</script>

<style>
.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

textarea {
    width: 100%;
    height: 100px;
}
</style>

  