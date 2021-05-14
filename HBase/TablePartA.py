import happybase as hb             

connection = hb.Connection()

connection.create_table('powers',
                    {'personal': dict(),
                     'professional': dict(),
                     'custom': dict()
                    })

connection.create_table('food',
                    {'fcf1': dict(),
                     'fcf2': dict()
                    })


