def format_records(lst):
    if len(lst) == 0:
        return "Empty record."
    records = []
    for record in lst:
        records.append(f'<a href="update/{record.id}/">Edit</a> {str(record)}')
    return "<br/>".join(records)
