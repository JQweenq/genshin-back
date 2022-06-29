import unittest

from app import create_app
from app.extensions import db
from app.models import WishCharacterFiveAssociationData, WishCharacterFiveAssociation, WishCharacterFourAssociationData, \
    WishCharacterFourAssociation
from app.models.character import Character, CharacterData
from app.models.wish import Wish, WishData


class WishModelCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('test')
        self.app_context = self.app.app_context()

        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_relationship(self):
        characters_4 = [
            Character(
                CharacterData(
                    name="Тартилия",
                    rarity=5,
                    name_en="Tartalia",
                    full_name="Аякс",
                    card="https://media.discordapp.net/attachments/771051943559823413/986701360999313418/unknown.png",
                    weapon="Лук",
                    eye="Гидро",
                    sex="Мужской",
                    birthday="20 июля",
                    region="Снежная",
                    affiliation="Фатуи",
                    portrait="https://media.discordapp.net/attachments/771051943559823413/986701407048572938/unknown.png?width=248&height=473",
                    description="Познакомьтесь с Тартальей, непредсказуемым воином из Снежной! Не питайте иллюзий, что вы понимаете его подлинные намерения. Не забывайте, что за этой невинной внешностью скрывается безжалостное орудие для убийства."
                )
            ),
            Character(
                CharacterData(
                    name="Кэ Цин",
                    rarity=5,
                    name_en="keqing",
                    card="https://cdn.discordapp.com/attachments/771051943559823413/986701552603508776/unknown.png",
                    weapon="Меч",
                    eye="Электро",
                    sex="Женский",
                    birthday="20 ноября",
                    region="Снежная",
                    affiliation="Цисин",
                    portrait="https://cdn.discordapp.com/attachments/771051943559823413/986701577156964402/unknown.png",
                    description="Юй Хэн группировки Цисин в Ли Юэ. У неё есть что сказать против «Властелина камня, правящего Ли Юэ лишь словом», но, оказывается, боги любят таких скептиков, как она. Она твёрдо верит: судьбу человечества должно вершить само человечество, ведь человек лучше знает, что нужно его роду. Чтобы доказать это, она работает так усердно, как никто другой."
                )
            ),
            Character(
                CharacterData(
                    name="Чжун Ли",
                    rarity=5,
                    name_en="zhongli",
                    full_name="Аякс",
                    card="https://cdn.discordapp.com/attachments/771051943559823413/986701626217742336/unknown.png",
                    weapon="Копьё",
                    eye="Гео",
                    sex="Мужской",
                    birthday="31 декабря",
                    region="Ли Юэ",
                    affiliation="Ритуальное Бюро «Ваншэн»; Архонты",
                    portrait="https://cdn.discordapp.com/attachments/771051943559823413/986701670882902087/unknown.png",
                    description="Загадочный консультант ритуального бюро «Ваншэн». Красив, обладает изящными манерами и выдающимся интеллектом. Происхождение Чжун Ли неизвестно, но он отлично знаком с правилами этикета и хорошими манерами. В ритуальном бюро «Ваншэн» он занимается проведением церемоний любого рода."
                )
            )
        ]
        character_5 = Character(
            CharacterData(
                name="Гань Юй",
                rarity=5,
                name_en="ganyu",
                full_name="Аякс",
                card="https://cdn.discordapp.com/attachments/771051943559823413/986701725475950702/unknown.png",
                weapon="Лук",
                eye="Крио",
                sex="Женский",
                birthday="2 декабря",
                region="Ли Юэ",
                affiliation="Павильон Лунного моря",
                portrait="https://cdn.discordapp.com/attachments/771051943559823413/986701748657860628/unknown.png",
                description="Главный секретарь Цисин. В её жилах течёт кровь божественного зверя. Гань Юй от природы спокойна и грациозна, но мягкий характер мифического зверя цилиня решительности и трудолюбию нисколько не противоречит. В конце концов, Гань Юй убеждена, что её работа - следовать контракту с Властелином Камня, то есть стремиться к благополучию всех живых существ в Ли Юэ."
            )
        )

        wish = Wish(
            WishData(
                title="Пиршество они",
                version="2.7",
                poster="https://cdn.discordapp.com/attachments/771051943559823413/991711321466880100/unknown.png"
            )
        )

        db.session.add_all(characters_4)
        db.session.add_all([character_5, wish])

        db.session.commit()

        four_associations = []

        for character_4 in characters_4:
            four_association = WishCharacterFourAssociation(WishCharacterFourAssociationData())
            four_association.character_id = character_4.id
            four_association.wish_id = wish.id
            four_associations.append(four_association)

        five_association = WishCharacterFiveAssociation(WishCharacterFiveAssociationData())
        five_association.character_id = character_5.id
        five_association.wish_id = wish.id

        db.session.add_all(four_associations)
        db.session.add(five_association)
        db.session.commit()

        self.assertTrue(db.session.query(Wish).all() != [])
