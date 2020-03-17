/**
 * @file AllTests.java
 * @author Jay Mody
 * @brief Runs all the unit testing modules.
 * @date 16/03/20 (dd/mm/yy)
 */

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
    TestPointT.class,
    TestLanduseMapT.class,
    TestDemT.class
})

public class AllTests {
}
