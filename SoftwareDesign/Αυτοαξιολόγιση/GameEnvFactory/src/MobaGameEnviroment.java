package GameEnvFactory.src;

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