data = """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"""
