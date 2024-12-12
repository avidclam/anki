from pathlib import Path
from .config import Config, defaults


def read_path(path):
    return Path(path).read_text(encoding='utf-8')


def load_design(dir: Path) -> Config:
    cfg = Config()
    cfg['css'] = '\n'.join(p.read_text() for p in dir.glob('*.css'))
    # Read html cards
    default_card = {}
    card_collection = {}
    for card_path in dir.glob('*.[black|front]*.html'):
        name, side = card_path.stem.rsplit('.', 1)
        if name == defaults['design.default']:
            default_card[side] = read_path(card_path)
        else:
            if name not in card_collection:
                card_collection[name] = {}
            card_collection[name][side] = read_path(card_path)
        # Set defaults
        for name in card_collection:
            if 'back' not in card_collection[name]:
                card_collection[name]['back'] = default_card.get('back', '')
            if 'front' not in card_collection[name]:
                card_collection[name]['front'] = default_card.get('front', '')
        cfg['card'] = card_collection
    return cfg