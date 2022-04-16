package GameEnvFactory.src;

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