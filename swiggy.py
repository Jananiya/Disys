Restaurant=[{"Restaurant_name":"Seasonal Tastes","Restaurant_num":7397266887,"Rating":4.0,"Food_prefernce":"Tandoori chicken"},                       #DICTIONARY INSIDE LIST
           {"Restaurant_name":"Teppan - Japanese Restaurant","Restaurant_num":7305341565,"Rating":4.3,"Food_prefernce":"sushi"},
           {"Restaurant_name":"Sunset Grill","Restaurant_num":6381347949,"Rating":4.1,"Food_prefernce":"BBQ chicken"},
           {"Restaurant_name":"Madras Pavilion","Restaurant_num":7358355054,"Rating":4.5,"Food_prefernce":"Malai chicken"},
           {"Restaurant_name":"Dakshin","Restaurant_num":7200636126,"Rating":4.5,"Food_prefernce":"fish finger"},
           {"Restaurant_name":"The Flying Elephant","Restaurant_num":9597916931,"Rating":4.4,"Food_prefernce":"chicken rice"},
           {"Restaurant_name":"Soy Soi","Restaurant_num":8056469214,"Rating":4.4,"Food_prefernce":"sushi"},
           {"Restaurant_name":"Avartana","Restaurant_num":9962454833,"Rating":4.7,"Food_prefernce":"Noodles"},
           {"Restaurant_name":"Peshawri","Restaurant_num":8015341851,"Rating":4.4,"Food_prefernce":"chicken curry"},
           {"Restaurant_name":"Bazaar","Restaurant_num":7305624091,"Rating":4.2,"Food_prefernce":"panner grill"},
           {"Restaurant_name":"Benjarong","Restaurant_num":8939509826,"Rating":4.4,"Food_prefernce":"shawarma"},
           {"Restaurant_name":"Basil With A Twist","Restaurant_num":6369121983,"Rating":4.8,"Food_prefernce":"mac and cheese"},
           {"Restaurant_name":"writter's cafe","Restaurant_num":9833807044,"Rating":4.0,"Food_prefernce":"pizza"},
           {"Restaurant_name":"Crimson Chakra","Restaurant_num":9941297487,"Rating":4.7,"Food_prefernce":"chocotruffle"},
           {"Restaurant_name":"bagavathi","Restaurant_num":7200001990,"Rating":"personal","Food_prefernce":"regular"},
           {"Restaurant_name":"Kayal","Restaurant_num":6382880108,"Rating":3.9,"Food_prefernce":"chicken machurian"},
           {"Restaurant_name":"Chipstead","Restaurant_num":9941656319,"Rating":4.1,"Food_prefernce":"BBQ"},
           {"Restaurant_name":"Roast & Grills","gpaynum":9500075619,"Rating":4.8,"Food_prefernce":"fish BBQ"},
           {"Restaurant_name":"Board Walk","Restaurant_num":8072512570,"Rating":4.1,"Food_prefernce":"mutton curry"},
           {"Restaurant_name":"Hablife Novella","Restaurant_num":6382761961,"Rating":3.8,"Food_prefernce":"veg burger"},
           {"Restaurant_name":"China XO","Restaurant_num":9791045340,"Rating":4.5,"Food_prefernce":"Chicken noodles"},
           {"Restaurant_name":"Flying Elephant","Restaurant_num":9841032642,"Rating":4.0,"Food_prefernc":"chicken BBQ"},
           {"Restaurant_name":"Bay View","Restaurant_num":6383908036,"Rating":4.9,"Food_prefernc":"cheese balls"},
           {"Restaurant_name":"dharan","Restaurant_num":8248631340,"Rating":"personal","Food_prefernc":"rare"},
           {"Restaurant_name":"divya","Restaurant_num":6374339918,"Rating":"personal","Food_prefernc":"regular"},
           {"Restaurant_name":"doss","Restaurant_num":9840644601,"Rating":"personal","Food_prefernc":"regular"},
           {"Restaurant_name":"durka","Restaurant_num":6379741175,"Rating":"personal","Food_prefernc":"regular"},
           {"Restaurant_name":"esther","Restaurant_num":8124252926,"Rating":"personal","Food_prefernc":"regular"},
           {"Restaurant_name":"femila","Restaurant_num":9176093745,"Rating":"personal","Food_prefernc":"regular"},
           {"Restaurant_name":"gautam","Restaurant_num":9176358088,"Rating":"personal","Food_prefernc":"regular"},
           {"Restaurant_name":"gayathri","Restaurant_num":7305331140,"Rating":"personal","transaction":"rare"},
           {"Restaurant_name":"gomathi","Restaurant_num":6384316771,"Rating":"personal","transaction":"regular"},
           {"Restaurant_name":"gracy","Restaurant_num":9150381712,"Rating":"personal","transaction":"regular"}]
for i in Restaurant:
    for j,k in i.items():
        print(f"{j}:{k}")
