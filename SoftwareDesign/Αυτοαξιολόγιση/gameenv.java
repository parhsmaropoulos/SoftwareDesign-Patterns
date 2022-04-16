
/**
 * Test class for the abstract game factory pattern.
 */
public class gameenv {

    public void main(String arg[]) {

        // Create MOBA game object
        GameElementFactory MobaGame = new MobaGameEnviroment();
        // Create player and obstacles
        Player mobaPlayer = MobaGame.createPlayer();
        Obstacle mobaOstacle = MobaGame.createObstacle();

        // Create FPS game object
        GameElementFactory FpsGame = new FPSGameEnviroment();
        // Create player and obstacles
        Player fpsPlayer = FpsGame.createPlayer();
        Obstacle fpsObstacle = FpsGame.createObstacle();

    }

    /**
     * Declares an interface for operations that create abstract game enviroment
     * objects.
     */
    public interface GameElementFactory {
        Player createPlayer();

        Obstacle createObstacle();

    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the SinglePlayer interface.
     */
    public class ObstacleSingle implements Obstacle {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the SinglePlayer interface.
     */
    public class PlayerSingle implements Player {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the MultiPlayer interface.
     */
    public class ObstacleMultiple implements Obstacle {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the MultiPlayer interface.
     */
    public class PlayerMultiple implements Player {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the MOBA interface.
     */
    public class ObstacleMoba implements Obstacle {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the MOBA interface.
     */
    public class PlayerMoba implements Player {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the FPSgame interface.
     */
    public class ObstacleFPS implements Obstacle {
    }

    /**
     * Defines a product object to be created by the corresponsing concrete factory.
     * Implements the FPSgame interface.
     */
    public class PlayerFPS implements Player {
    }

    public interface Player {

    }

    public interface Obstacle {

    }

    /**
     * Implements the operations to create game product objects.
     */
    public class SinglePlayerGameEnviroment implements GameElementFactory {
        public Player createPlayer() {
            return new PlayerSingle();
        };

        public Obstacle createObstacle() {
            return new ObstacleSingle();
        };
    }

    /**
     * Implements the operations to create game product objects.
     */
    public class MultiPlayerGameEnviroment implements GameElementFactory {
        public Player createPlayer() {
            return new PlayerMultiple();
        };

        public Obstacle createObstacle() {
            return new ObstacleMultiple();
        };
    }

    /**
     * Implements the operations to create game product objects.
     */
    public class MobaGameEnviroment implements GameElementFactory {
        public Player createPlayer() {
            return new PlayerMoba();
        };

        public Obstacle createObstacle() {
            return new ObstacleMoba();
        };
    }

    /**
     * Implements the operations to create game product objects.
     */
    public class FPSGameEnviroment implements GameElementFactory {
        public Player createPlayer() {
            return new PlayerFPS();
        };

        public Obstacle createObstacle() {
            return new ObstacleFPS();
        };
    }

}
