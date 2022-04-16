package GameEnvFactory.src;

// /**
//  * Declares an interface for a type of product object.
//  */
// public interface SinglePlayer {
// }

// /**
//  * Declares an interface for a type of product object.
//  */
// public interface MultiPlayer {
// }

// /**
//  * Declares an interface for a type of product object.
//  */
// public interface FPSgame {
// }

// /**
//  * Declares an interface for a type of product object.
//  */
// public interface MOBA {
// }

// /**
//  * Declares an interface for operations that create abstract game enviroment
//  * objects.
//  */
// public interface GameElementFactory {
//     SinglePlayer createSinglePlayer();

//     MultiPlayer createMultiPlayer();

//     FPSgame createFPSgame();

//     MOBA createMoba();

// }

/**
 * Test class for the abstract game factory pattern.
 */
public class App {
    public static void main(String arg[]) {
        GameElementFactory factory = new GameElementFactory();
        FPSgame fps = factory.createFPSgame();
        MOBA moba = factory.createMoba();
        SinglePlayer single_player = factory.createSinglePlayer();
        MultiPlayer multi_player = factory.createMultiPlayer();

    }
}
