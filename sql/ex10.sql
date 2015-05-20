SELECT * FROM pet;

UPDATE pet SET name = "Zed's Pet" WHERE id IN(
	SELECT pet.id FROM pet, person_pet, person
	WHERE 
	person_pet.person_id = person.id AND
	pet.id = person_pet.pet_id AND
	person.first_name = "Zed"
);

SELECT * FROM pet;