package GameEnvFactory.src;

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