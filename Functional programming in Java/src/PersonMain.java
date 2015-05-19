/**
 * Created by Kristian on 19/05/15.
 */

import java.util.ArrayList;
import java.util.List;

public class PersonMain {
    List<Person> persons = new ArrayList<Person>();

    public void init() {
        persons.add(new Person("Ola", 10, 'M'));
        persons.add(new Person("Kari", 12, 'F'));
        persons.add(new Person("Per", 22, 'M'));
        persons.add(new Person("Pål", 17, 'M'));
        persons.add(new Person("Espen", 19, 'M'));
    }

    public void run() {
        LambdaFunctions lf = new LambdaFunctions();
        System.out.println(persons);
        lf.sortByAge(persons);
        System.out.println(persons);
        lf.sortByName(persons);
        System.out.println(persons);
        System.out.println(lf.map(persons));
        System.out.println(lf.reduce(persons));
        lf.filterForEach(persons);
        System.out.println(persons);
        System.out.println(lf.reduce(persons));

    }


    public static void main(String[] args) {
        PersonMain program = new PersonMain();
        program.init();
        program.run();
    }


}