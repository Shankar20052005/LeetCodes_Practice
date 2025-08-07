select email from Person where email is not null
group by email
having count(email)>1;