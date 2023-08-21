def SearchingChallenge(strParam):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  validChars = 'abcdefghijklmnopqrstuvwxyz0123456789_'

  if len(strParam) < 4 or len(strParam) > 25:
    return 'false'

  if strParam[0].lower() not in alphabet:
    return 'false'

  for i in range(len(list(strParam))):
    if strParam[i].lower() not in validChars:
      return 'false'

  if strParam[len(strParam)-1] == '_':
    return 'false'

  return 'true'
  