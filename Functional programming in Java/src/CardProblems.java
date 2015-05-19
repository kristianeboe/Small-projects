import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.stream.Collector;
import java.util.stream.Collectors;

/**
 * Created by Kristian on 19/05/15.
 */
public class CardProblems {

    public static void main(String[] args) {
        Collection<Card> cards = Arrays.asList(new Card('S', 1), new Card('H', 2), new Card('D', 12), new Card('C', 13));
        CardProblems cp = new CardProblems();
        cp.filterSpades(cards);
        cp.mapSuits(cards);
        cp.mapSuits2(cards);
        cp.reduceFaces(cards);
        cp.anyMatchSuit(cards, 'S');
    }

    public void filterSpades(Collection<Card> cards) {
        System.out.println(cards.stream().filter(c -> c.getSuit() == 'S').collect(Collectors.toList()));
    }

    public void mapSuits(Collection<Card> cards) {
        System.out.println(cards.stream().map(c-> c.getSuit()).collect(Collectors.toList()));
    }

    public void mapSuits2(Collection<Card> cards) {
        System.out.println(cards.stream().map(Card::getSuit).collect(Collectors.toList()));
    }

    public void reduceFaces(Collection<Card> cards){
        System.out.println(cards.stream().map(Card::getFace).reduce((a,b)->(a+b)).get());
    }

    public void anyMatchSuit(Collection<Card> cards, char suit){
        System.out.println(cards.stream().anyMatch(c -> c.getSuit()==suit));
    }

}
