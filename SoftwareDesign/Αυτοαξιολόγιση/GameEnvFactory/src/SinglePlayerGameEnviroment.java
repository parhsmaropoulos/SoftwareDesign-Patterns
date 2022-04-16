package GameEnvFactory.src;

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