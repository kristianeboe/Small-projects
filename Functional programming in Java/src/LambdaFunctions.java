import org.w3c.dom.ls.LSException;

import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by Kristian on 19/05/15.
 */
public class LambdaFunctions {

    public List<Person> sortByName(List<Person> persons) {
        persons.sort((a, b) -> a.getName().compareTo(b.getName()));
        return persons;
    }

    public List<Person> sortByAge(List<Person> persons) {
        persons.sort((a, b) -> a.getAge() - b.getAge());
        return persons;
    }

    public boolean anyMatch(List<Person> persons){
        return persons.stream().anyMatch((p-> p.getGender() == 'F'));
    }

    public List<Person> filter(List<Person> persons){
        return persons.stream().filter(p -> p.getAge() >= 18).collect(Collectors.toList());
    }

    public List<Integer> map(List<Person> persons){
        return persons.stream().map(Person::getAge).collect(Collectors.toList());
    }

    public int reduce(List<Person> persons){
        return map(persons).stream().reduce((a, b) -> a + b).get();
    }

    public void forEach(List<Person> persons) {
        persons.stream().forEach(p -> p.setAge(p.getAge()+1));
    }

    public List<Person> peek(List<Person> persons) {
        return persons.stream().peek(p->p.setAge(p.getAge()+1)).collect(Collectors.toList());
    }

    public void filterForEach(List<Person> persons){
        persons.stream().filter(p -> p.getAge() >= 18 && p.getGender() == 'M').forEach(p -> p.setAge(p.getAge()+1));
    }



}
