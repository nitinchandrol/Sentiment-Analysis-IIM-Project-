feature_list=["price", "picture","battery","storage", "upgrade","hardware","feature","size","design","media","sound","service","help-care","overall"]
feature= [

['dollar', 'worth', 'cost', 'range', 'expensive','cheap', 'budget', 'value','price','rupee'],

['videos', 'scan', 'photo', 'blur','photography', 'video', 'flush', 'camera', 'pixel', 'picture', 'image', 'zoom','resolution'],

['charge', 'charging', 'battery', 'discharge', 'backup','rechagre','adapter'],

['build','memory','gb','mb','kb','capacity', 'ram','processing','core','processor'],

['advance', 'upgrade', 'improvement', 'version', 'upgrded'],

['hardware','screen','display','dial', 'key','button'],

['bluetooth','wifi','usb','gprs','function','menu','option','setting'],

['heavy', 'bulky', 'weight', 'massive', 'light', 'size','small'],

['shape','style','looks','design','interface','color', 'colour','layout'],

['internet','gaming', 'game','apps','radio','web','movie','fm','map'  ],

['song','beat', 'tone', 'headphone', 'music', 'sound', 'earphone', 'speaker', 'audio','volume','voice','ring'],

['experience','log', 'reception','signal','network', 'bill', 'packaging', 'service', 'ordering', 'offer', 'delivery', 'packing', 'performance', 'review','defective','deliver',"delay",'phonebook','software'],

['support', 'facility','help', 'care','help-line','trust','maintenance','portability','tech','kit','manual'],

['phone','feature','better','average','genral','overall','like','good']
]

new_syn = [['run', 'chain', 'price', 'flash', 'rate', 'cost', 'flashy', 'order'], ['even', 'picture', 'videos', 'photo', 'boot', 'solution', 'fancy', 'range', 'video'], ['direction', 'bill', 'run', 'billing', 'point', 'support', 'drop', 'boot', 'file', 'care'], ['capability', 'march', 'center', 'form', 'process', 'make', 'work', 'storage', 'drive', 'content', 'force', 'store'], ['advance', 'upgrade', 'win', 'improvement', 'rendering', 'reading'], ['cover', 'name'], ['do', 'use', 'set', 'run', 'office', 'settings', 'work', 'choice', 'part', 'go', 'occasion', 'mark', 'card'], ['sound', 'great', 'angle', 'big', 'little', 'lighting', 'low', 'easy'], ['count', 'search', 'configuration', 'tone', 'look', 'form', 'title', 'color', 'colour', 'work', 'looking', 'feel', 'feels', 'aspect', 'build', 'way', 'innovation', 'front', 'wait', 'expression', 'mode'], ['function', 'picture', 'play', 'back', 'wireless', 'game', 'net'], ['feel', 'phones', 'headphone', 'looks', 'go', 'quality', 'earpiece', 'speakers', 'note', 'book', 'call', 'good', 'get', 'bulk', 'phone', 'feels', 'part', 'sound', 'audio', 'look', 'step', 'voice', 'pack'], ['saving', 'help', 'point', 'feel', 'rate', 'have', 'go', 'check', 'compact', 'web', 'note', 'net', 'notice', 'offering', 'get', 'stay', 'feels', 'response', 'card', 'wait', 'package', 'reviews', 'range', 'order', 'pack'], ['installation', 'service', 'deal', 'back', 'like', 'caution', 'bank', 'keep', 'backup', 'hope', 'care'], ['sound', 'good', 'features', 'just', 'media', 'well', 'headphone', 'call', 'earpiece', 'have', 'phones', 'mean', 'best', 'care']]
new_hyp = [['move', 'capability', 'set', 'installation', 'facility', 'bill', 'ideal', 'value', 'note', 'go', 'amount', 'cost', 'ask', 'quality', 'worth'], ['set', 'color', 'move', 'course', 'go', 'speed', 'process', 'conclusion', 'picture', 'product', 'someone', 'run', 'description', 'job', 'imagine', 'line', 'change', 'search', 'colour', 'recording', 'person', 'model'], ['set', 'cost', 'material', 'collection', 'voice', 'duplicate', 'stuff', 'device', 'part', 'trust', 'speed', 'change', 'conclusion'], ['function', 'hardware', 'capability', 'set', 'center', 'deal', 'process', 'volume', 'make', 'body', 'content', 'person', 'someone', 'stuff', 'power', 'better', 'touch', 'found', 'part', 'office', 'care'], ['status', 'motion', 'set', 'rate', 'package', 'support', 'move', 'range', 'side', 'hardware', 'amount', 'better', 'go', 'improvement', 'order', 'software'], ['canvas', 'space', 'surface', 'display', 'device', 'check'], ['move', 'do', 'set', 'service', 'package', 'make', 'bill', 'schedule', 'change', 'software'], ['status', 'look', 'surface', 'part', 'aspect', 'device', 'expression', 'class', 'friend', 'size'], ['tone', 'process', 'surface', 'design', 'touch', 'trust', 'quality', 'check', 'end', 'ordering', 'make', 'system', 'call', 'bank', 'body', 'do', 'direction', 'form', 'material', 'change', 'care', 'kind', 'name', 'work', 'stuff', 'order', 'mean'], ['picture', 'play', 'section', 'material', 'metal', 'product', 'competition', 'system', 'job', 'score', 'design', 'part', 'line'], ['chain', 'color', 'move', 'play', 'touch', 'rate', 'go', 'utter', 'quality', 'make', 'platform', 'way', 'product', 'buy', 'form', 'express', 'delivery', 'line', 'sound', 'look', 'colour', 'work', 'bargain', 'recording', 'amount', 'piece', 'expression'], ['work', 'force', 'help', 'process', 'move', 'system', 'have', 'go', 'utter', 'check', 'market', 'compact', 'canvas', 'feature', 'content', 'wait', 'company', 'function', 'run', 'power', 'get', 'couple', 'material', 'hand', 'delivery', 'post', 'change', 'name', 'case', 'remember', 'gift', 'getting', 'drop', 'record', 'stuff', 'care'], ['case', 'advance', 'play', 'help', 'service', 'keep', 'support', 'work', 'mind', 'hand', 'better', 'reason', 'part', 'want', 'device', 'voice', 'check', 'proof'], ['picture', 'product', 'good', 'advantage', 'form', 'superior', 'kind', 'number', 'amount', 'have', 'total', 'quality', 'change', 'want']]
