def calPoints(self, operations: List[str]) -> int:
  record = []
  for i in range(len(operations)):
      if operations[i] == "+":
          new = record[-1] + record[-2]
          record.append(new)

      elif operations[i] == "D":
          new = record[-1] * 2
          record.append(new)

      elif operations[i] == "C":
          record.pop()
      else:
          new = int(operations[i])
          record.append(new)
          
  
  return sum(record)