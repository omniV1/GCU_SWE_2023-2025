(() => {
let scores: number[] = [85, 90, 78]; 

    for(let i = 0; i < scores.length; i++)
       {
           console.log(`Score ${i + 1}: ${scores[i]}`); 
       }
    
let count: number = 0; 
    while (count < 3)
        {
            console.log(`Count: ${count}`); 
            count++;
        }
    
let languages: string[] = ["TypeScript", "Java", "CSharp"]; 
     for (let lang of languages)
        {
           console.log(lang); 
        }

let person = {name: "Owen", age: 26 }; 
     for (let key in person)
        {
            console.log(`${key}: ${person[key as keyof typeof person]}`); 
        }
  })();