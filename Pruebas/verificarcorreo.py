import dns.resolver
import dkim

def get_spf_record(domain):
    try:
        answers = dns.resolver.query(domain, 'TXT')
        for rdata in answers:
            txt_record = rdata.strings
            for record in txt_record:
                if record.startswith('v=spf1'):
                    return record
        return None
    except dns.resolver.NXDOMAIN:
        return None

def verify_dkim_signature(message, signature):
    try:
        return dkim.verify(message, signature)
    except dkim.DkimKeyError:
        return False

# Dominio para verificar
domain_to_check = "juandapilo@gmail.com"

# Verificar registro SPF
spf_record = get_spf_record(domain_to_check)
if spf_record:
    print(f"Registro SPF para {domain_to_check}: {spf_record}")
else:
    print(f"No se encontró registro SPF para {domain_to_check}")