class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    def get_number_of_watches_created(self):
        return self.watches_created

    @classmethod
    def engraving(cls, text):
        if len(text) >= 40:
            raise Exception('Engraving text is over 40 characters')
            
        if not text.isalnum():
            raise Exception('Engraving text is not alphanumeric')
        
        _watch = cls()
        _watch.engraving = text
        return _watch
        
try:
    print(f"Number of watches: {LuxuryWatch.watches_created}")
    w1 = LuxuryWatch()
    print(f"Number of watches: {LuxuryWatch.watches_created}")
    w2 = LuxuryWatch.engraving('lifewithoutwater')
    print(f"Number of watches: {LuxuryWatch.watches_created}")
    w3 = LuxuryWatch.engraving('foo@baz.com')
    print(f"Number of watches: {LuxuryWatch.watches_created}")
except Exception as e:
    print(f"Error: {e}")

