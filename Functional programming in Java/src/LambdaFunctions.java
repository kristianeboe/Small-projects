import java.util.List;

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


}
