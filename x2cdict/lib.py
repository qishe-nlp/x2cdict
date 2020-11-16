from x2cdict.pos_map import POSMAP

def gen_dictname(from_lang, to_lang):
  return "{}2{}".format(from_lang, to_lang)

def formalize_record(result, lang):
  e = {}
  if result != None:
    e['meaning'] = result['explanation']['meaning']
    e['dict_pos'] = result['explanation']['pos']
    e['from'] = result['from']
    if e['dict_pos'] not in POSMAP[lang]['VERB']:
      e['extension'] = result['explanation']['extension'] if 'extension' in result['explanation'].keys() else None
      e['variations'] = None
    else:
      e['extension'] = result['extension'] if 'extension' in result.keys() else None
      e['variations'] = result['variations'] if 'variations' in result.keys() else None
  return e
